#/usr/bin/env python
# -*- coding: utf-8 -*-

from network.tools import *
from config.Configures import configures
import threading
from gpio.GPIO import GPIO
import socket
import logging
from network.Recv import Recv
import datetime
import serial

class Network(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.data = ""

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

    def run(self):

        # 红色报警灯
        relayR = 15
        # 停带
        relayStop = 12

        # set socket server
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(('', 8088))
        sock.listen(5)

        while True:
            try:
                connection, address = sock.accept()

                Recv.receiveThreadStatus = True 
                receive = Recv()
                receive.setConnection(connection)
                receive.start()

                sendHeartbeatCount = 0
                recvHeartbeatCount = 0

                while True:
                    try:
                        if len(self.data) != 0:
                            print(self.data)

                            if Recv.running:

                                if len(self.data) == 32:
                                    # 3-8位是产品代码，17-22位是生产日期，041204， 代表2004-12-04
                                    if (True if "999999" == Recv.productCode else self.data[2:8] == Recv.productCode) and ((datetime.date(int("20" + self.data[16:18]), int(self.data[18:20]), int(self.data[20:22])) -  Recv.checkDate).days > 0) :
                                        count = connection.send(bytes("T1C103" + "%04d" % len(self.data) + self.data + "1\r\n", encoding="utf8"))
                                    else:
                                        count = connection.send(bytes("T1C103" + "%04d" % len(self.data) + self.data + "0\r\n", encoding="utf8"))

                                if len(self.data) == 6:
                                    count = connection.send(bytes("T1C103" + "%04d" % len(self.data) + self.data + "\r\n", encoding="utf8"))

                                self.data = ""

                        if Recv.receiveThreadStatus != True :
                            break

                        sendHeartbeatCount += 1
                        if (sendHeartbeatCount % 1000 == 0):
                            sendHeartbeatCount = 0
                            count = connection.send(bytes("T1C1990002\r\n", encoding="utf8"))

                        recvHeartbeatCount += 1
                        if(Recv.recvHeartbitFlag == True):
                            recvHeartbeatCount = 0
                        # 20 seconds can't get heartbeat, will close the connect.
                        if(recvHeartbeatCount >= 2000):
                            break

                        time.sleep(0.01)
                    except:
                        logging.debug("receive data except. ")
                        break;

                connection.close()
                logging.debug('send thread disconnection')
            except :
                logging.debug('send thread except')

        serialOut.close()

