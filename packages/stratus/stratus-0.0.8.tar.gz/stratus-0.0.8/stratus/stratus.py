#! /usr/bin/python
import socket
import json
import urllib
import ssl
import Cookie
import argparse
import thread
import os
import sys
import urllib
import traceback
import mimetypes
import datetime
import time
import SimpleHTTPSServer
import copy
import httplib

import sockhttp

VERSION = "0.0.8"
PORT = 5678
ALL_CLIENTS = "__all__"


class server(SimpleHTTPSServer.handler):
    """docstring for handler"""
    def __init__(self):
        super(server, self).__init__()
        self.node_timeout(1, 60)
        self.conns = {}
        self.clients = {}
        self.data = {}
        self.online = 0
        self.actions = [
            ('post', '/ping/:name', self.post_ping),
            ('get', '/ping/:name', self.get_ping),
            ('get', '/connect/:name', self.get_connect),
            ('get', '/messages/:name', self.get_messages),
            ('get', '/connected', self.get_connected),
            ('get', '/:page', self.get_connected)
            ]

    def log(self, message):
        del message

    def date_handler(self, obj):
        return obj.isoformat() if hasattr(obj, 'isoformat') else obj

    def post_ping(self, request):
        self.node_status(request["variables"]["name"], update=True)
        # Add message to be sent out
        recv_data = self.form_data(request['data'])
        recv_data = self.message(request["variables"]["name"], \
            recv_data["data"], recv_data["to"])
        self.add_message(recv_data)
        thread.start_new_thread( self.send_messages, (recv_data["to"], ))
        # Get messages for sender
        return self.get_messages(request)

    def get_ping(self, request):
        self.node_status(request["variables"]["name"], update=True)
        # Get messages for sender
        return self.get_messages(request)

    def get_connect(self, request):
        self.node_status(request["variables"]["name"], update=True, \
            conn=request["socket"])
        # Get messages for sender
        return self.get_messages(request)

    def get_messages(self, request):
        # Get messages for sender
        send_data = self.messages(request["variables"]["name"])
        output = json.dumps(send_data)
        headers = self.create_header()
        headers["Content-Type"] = "application/json"
        return self.end_response(headers, output)

    def get_connected(self, request):
        output = json.dumps(self.clients, default=self.date_handler)
        headers = self.create_header()
        headers["Content-Type"] = "application/json"
        return self.end_response(headers, output)

    def start_server(self, address="0.0.0.0", port=PORT, key=False, crt=False):
        thread.start_new_thread(self.update_status, ())
        server_process = SimpleHTTPSServer.server((address, port), self, \
            bind_and_activate=False, threading=True, \
            key=key, crt=crt)
        return thread.start_new_thread(server_process.serve_forever, ())

    def update_status(self):
        while True:
            for node in self.clients:
                self.node_status(node)
            time.sleep(self.timeout_seconds)

    def node_status(self, node_name, update=False, conn=False):
        curr_time = datetime.datetime.now()
        if not node_name in self.clients:
            self.clients[node_name] = self.node(node_name, curr_time)
            self.online += 1
        elif update:
            self.clients[node_name]["last_update"] = curr_time
            self.clients[node_name]["online"] = True
            if not self.clients[node_name]["online"]:
                self.online += 1
        else:
            if curr_time - self.timeout > \
                self.clients[node_name]["last_update"]:
                self.clients[node_name]["online"] = False
                self.online -= 1
        if conn:
            self.conns[node_name] = conn

    def node(self, name, curr_time=False):
        # Don't have to call datetime.datetime.now() is provided
        if not curr_time:
            curr_time = datetime.datetime.now()
        return {
            "name": name,
            "last_update": curr_time,
            "online": True
        }

    def message(self, sent_by, data, to=ALL_CLIENTS):
        return {
            "to": to,
            "from": sent_by,
            "data": data,
            "seen": [sent_by]
        }

    def add_message(self, add):
        if not add["to"] in self.data:
            self.data[add["to"]] = []
        self.data[add["to"]].append(add)

    def send_to(self, node_name, data):
        if node_name in self.conns:
            try:
                return self.conns[node_name].sendall(data)
            except:
                del self.conns[node_name]
        return False

    def send_messages(self, to):
        clients = []
        if to == ALL_CLIENTS:
            clients = list(self.conns.keys())
        else:
            clients = [to]
        for client_name in clients:
            thread.start_new_thread( self.send_message, (client_name, ))

    def send_message(self, to):
        # Get messages for to
        send_data = self.messages(to)
        output = json.dumps(send_data)
        headers = self.create_header()
        headers["Content-Type"] = "application/json"
        self.send_to(to, self.end_response(headers, output) )

    def messages(self, to):
        new_messages = []
        to_and_all = [to, ALL_CLIENTS]
        for name in to_and_all:
            if name in self.data:
                for item in self.data[name]:
                    # Check to see if everyone has seen this message
                    if not to in item["seen"]:
                        # Add to array of seen
                        item["seen"].append(to)
                        # Send the message without the seen array
                        append = copy.deepcopy(item)
                        del append["seen"]
                        new_messages.append(append)
                for item in xrange(0, len(self.data[name])):
                    if len(self.data[name]) and \
                        len(self.data[name][item]["seen"]) >= self.online:
                        del self.data[name][item]
        return new_messages

    def node_timeout(self, loop=False, delta=False):
        if loop:
            self.timeout_seconds = loop
            self.timeout = datetime.timedelta(seconds=loop)
        if delta:
            self.timeout = datetime.timedelta(seconds=delta)
        return self.timeout


class client(object):
    """docstring for client"""
    def __init__(self, host="localhost", port=PORT, protocol="http", \
        name=socket.gethostname(), update=20, recv=False):
        super(client, self).__init__()
        self.host = host
        self.port = port
        self.protocol = protocol
        self.name = name
        self.update = update
        self.recv = recv
        self.http_conncet()

    def http_conncet(self):
        """
        Connects to the server with tcp http connections.
        """
        values = (self.host, self.port, )
        host = "%s:%s" % values
        self.headers = {"Connection": "keep-alive"}
        self.ping_conn = httplib.HTTPConnection(host)
        self.send_conn = httplib.HTTPConnection(host)
        self.recv_conn = sockhttp.conn(self.host, self.port)
        return True

    def return_status(self, res):
        """
        Returns True if there was a json to pass to recv.
        """
        try:
            res = json.loads(res)
            if len(res) > 0 and self.recv:
                for item in xrange(0, len(res)):
                    res[item]["__name__"] = self.name
                    self.recv(res[item])
            return True
        except (ValueError, KeyError):
            return False

    def json(self, res):
        """
        Returns json if it can.
        """
        try:
            res = json.loads(res)
            return res
        except (ValueError, KeyError):
            return False

    def get(self, url, http_conn):
        """
        Requests the page and returns data
        """
        res = ""
        # try:
        http_conn.request("GET", "/" + url, headers=self.headers)
        res = http_conn.getresponse()
        res = res.read()
        # except (httplib.URLError, httplib.HTTPError), error:
        #     print error
        return res

    def post(self, url, data):
        """
        Requests the page and returns data
        """
        res = ""
        # try:
        headers = self.headers.copy()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
        data = urllib.urlencode(data, True).replace("+", "%20")
        self.send_conn.request("POST", "/" + url, data, headers)
        res = self.send_conn.getresponse()
        res = res.read()
        # except (httplib.URLError, httplib.HTTPError), error:
        #     print error
        return res

    def connect(self):
        """
        Starts main
        """
        return thread.start_new_thread(self.main, ())

    def main(self):
        """
        Continues to ping
        """
        self.recv_connect()
        while True:
            self.ping()
            time.sleep(self.update)
        return 0

    def recv_connect(self):
        """
        Connects a socket that the server can push to.
        """
        url = "/connect/" + self.name
        res = self.recv_conn.get(url)
        self.return_status(res)
        thread.start_new_thread( self.listen, () )

    def listen(self):
        while True:
            res = self.recv_conn.recv()
            if len(res):
                self.return_status(res)

    def ping(self):
        """
        Tells the server its still here and asks for instructions
        """
        url = "ping/" + self.name
        res = self.get(url, self.ping_conn)
        return self.return_status(res)

    def send(self, data, to=ALL_CLIENTS):
        """
        Queues data for sending
        """
        url = "ping/" + self.name
        if type(data) != str and type(data) != unicode:
            data = json.dumps(data)
        res = self.post(url, {"to": to, "data": data})
        return self.return_status(res)

    def connected(self):
        """
        Gets others connected
        """
        url = "connected"
        res = self.get(url, self.send_conn)
        return self.json(res)

    def online(self):
        """
        Gets others online
        """
        connected = self.connected()
        online = {}
        if connected:
            for item in connected:
                if connected[item]["online"]:
                    online[item] = connected[item]
        return online


def print_recv(data):
    print data

def main():
    address = "0.0.0.0"

    port = PORT
    if len(sys.argv) > 1:
        port = int(sys.argv[1])

    stratus_server = server()
    stratus_server.start_server(port=port)

    stratus_client_one = client(name="one")
    stratus_client_two = client(name="two")
    stratus_client_one.recv = print_recv
    stratus_client_two.recv = print_recv
    stratus_client_one.connect()
    stratus_client_two.connect()

    while True:
        data = raw_input("Send data: ")
        if len(data) > 0:
            stratus_client_one.send(data)
        pass


if __name__ == '__main__':
    main()
