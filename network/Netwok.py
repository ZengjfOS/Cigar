#/usr/bin/env python
# -*- coding: utf-8 -*-

from network.tools import *
from config.Configures import configures
import threading
from gpio.GPIO import GPIO

class Network(threading.Thread):

    def connect(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((configures.remoteConfig.ip, configures.remoteConfig.port))

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

    def setData(self, data):
        self.data = data

    def setSerial(self, serial):
        self.serial = serial

    def run(self):

        relayR = 15
        relayStop = 12

        if ping(configures.remoteConfig.ip) :
            self.connect()
            self.sendData(bytes(self.data, encoding = "utf8"))
            time.sleep(0.1%10)
            ret = self.resvData()[0]
            self.disconnect()

            if ret == 1:
                GPIO.setValue(relayR, 0)
                GPIO.setValue(relayStop, 0)
                time.sleep(2)
                GPIO.setValue(relayR, 1)
                GPIO.setValue(relayStop, 1)

            if ret == 0:
                GPIO.setValue(relayR, 1)
                GPIO.setValue(relayStop, 1)

                if (len(self.data) == 32) :
                    self.serial.write(bytes(self.data, encoding = "utf8"))

        else :
            if ping(configures.remoteConfig.ip) :
                self.connect()
                self.sendData(bytes(self.data, encoding = "utf8"))
                time.sleep(0.1%10)
                ret = self.resvData()[0]
                self.disconnect()

                if ret == 1:
                    GPIO.setValue(relayR, 0)
                    GPIO.setValue(relayStop, 0)
                    time.sleep(2)
                    GPIO.setValue(relayR, 1)
                    GPIO.setValue(relayStop, 1)

                if ret == 0:
                    GPIO.setValue(relayR, 1)
                    GPIO.setValue(relayStop, 1)

                    if (len(self.data) == 32) :
                        self.serial.write(bytes(self.data, encoding = "utf8"))

            # else :

            #     GPIO.setValue(relayR, 0)
            #     GPIO.setValue(relayStop, 0)
            #     time.sleep(0.5)
            #     GPIO.setValue(relayR, 1)
            #     GPIO.setValue(relayStop, 1)

