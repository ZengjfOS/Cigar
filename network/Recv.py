#/usr/bin/env python
# -*- coding: utf-8 -*-

from network.tools import *
from config.Configures import configures
import threading
from gpio.GPIO import GPIO
import logging
import re
# from datetime import *
import datetime

class Recv(threading.Thread):

    # 用于反应接收线程是否是正常，如果接收线程已经异常了，发送线程也就要退出了
    receiveThreadStatus = True
    # 是否开始校验
    running = False
    # 产品代码
    productCode = ""
    # 校验时间
    checkDate = datetime.date.today() - datetime.timedelta(days=180)
    # Heartbit
    recvHeartbitFlag = False

    def setConnection(self, conn):
        self.conn = conn

    def run(self):


        while True:
            try:
                buf = self.conn.recv(1024)
                bufstring = buf.decode("utf-8")
                print(buf)

                byteArrays = bufstring.split("\r\n")

                for bufstring in byteArrays:

                    if len(bufstring) <= 3:
                        continue

                    # send back to client
                    sendBytes = bytearray(bufstring + "\r\n", 'utf8')
                    sendBytes[0] = 0x54
                    sendBytes[2] = 0x43
                    # self.conn.send(sendBytes)

                    if re.search(r"C1T1010025RUN", bufstring) != None:

                        if len(bufstring) < 28 :
                            continue

                        self.conn.send(sendBytes)
                        Recv.running = True
                        Recv.productCode = bufstring[13:19]

                        try:
                            year  = int(bufstring[19:23])
                            month = int(bufstring[23:25])
                            day  = int(bufstring[25:27])
                            Recv.checkDate = datetime.date(year, month, day)
                        except:
                            logging.debug('receive date formate except.')
                            self.conn.send(bytearray("error\r\n", 'utf8'))


                    elif re.search(r"C1T1020006STOP", bufstring) != None:
                        self.conn.send(sendBytes)
                        Recv.running = False
                    elif re.search(r"C1T1990002", bufstring) != None:
                        Recv.recvHeartbitFlag = True

                time.sleep(0.01)

            except :
                logging.debug('receive thread except')
                break


        Recv.receiveThreadStatus = False

        time.sleep(1)
        self.conn.close()

        logging.debug('receive thread disconnection')
