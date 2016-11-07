#!/usr/bin/env python
# -*- coding: utf-8 -*-

from network.tools import *
from config.Configures import configures

class Network(object):

    def connect(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(configures.remoteConfig.ip, configures.remoteConfig.port)

    def sendData(self, data):
        if self.sock != None:
            self.sock.send(data)

    def resvData(self):
        if self.sock != None:
            return self.sock.recv(1024)

        return -1

    def disconnect(self):
        if self.sock != None:
            self.sock.close()

