#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import threading

RECV_BUFFER = 2048

class WriteThread(threading.Thread):
    global RECV_BUFFER

    def __init__(self, networkhandler, connection):
        self.connection = connection
        self.networkhandler = networkhandler
        threading.Thread.__init__(self)

    def run(self):
        while True:
            m = self.networkhandler.getoutmessage()
            self.connection.send(bytes(m, "utf8"))