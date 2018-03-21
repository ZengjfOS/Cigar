#!/usr/bin/env python
# -*- coding: utf-8 -*-

import getopt
import logging
import os
import sys
import time
import serial

from gpio.GPIO import GPIO
from shell.ShellCmd import ShellCmd
from network.tools import *
from config.Configures import configures
from network.Network import Network
from network.Recv import Recv
from uart.NportSwitch import NportSwitch
import datetime
import re
import DelayStop


def main(argv):

    try:
        opts, args = getopt.getopt(argv, "hct")
    except getopt.GetoptError:
        print("main.py [-h] [-c] [-t]")

        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':

            sys.exit()

        elif opt == "-c":

            sys.exit()

        elif opt == "-t":
            sys.exit()


    serialIn = serial.Serial("/dev/ttymxc2", configures.localConfig.scanBaudrate,
        timeout=1,
        bytesize=serial.EIGHTBITS,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE)

    serialOut = serial.Serial("/dev/ttymxc1", configures.localConfig.scanBaudrate,
        timeout=1,
        bytesize=serial.EIGHTBITS,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE)

    relayR = 15
    relayStop = 12
    GPIO.initGPIOOut(relayR, configures.localConfig.pindefvalue)
    GPIO.initGPIOOut(relayStop, configures.localConfig.pindefvalue)

    network = Network()
    network.start()

    NportSwitch().start()
    NportSwitch.setNportInPort(serialOut)
    NportSwitch.setSickOutPort(serialIn)

    while 1 :

        data = serialIn.readline()

        if len(data) <= 0 :
            continue

        if (re.search(r"\d{32}\r\n", data.decode()) != None) or (re.search(r"NoRead\r\n", data.decode()) != None):

            # 复位控制信号
            GPIO.setValue(relayR, configures.localConfig.pindefvalue)
            GPIO.setValue(relayStop, configures.localConfig.pindefvalue)
            realData = data.decode().replace('\r\n', '')

            if Recv.running == True:
                network.setData(realData)

            if len(data) == 8:
                serialOut.write(bytes(realData, encoding="utf8"))
                # DelayStop.DelayStop().start()

            if len(data) == 34:
                # 3-8位是产品代码，17-22位是生产日期，041204， 代表2004-12-04
                if (len(Recv.productCode) == 0 or realData[2:8] == Recv.productCode) and ((datetime.date(int("20" + realData[16:18]), int(realData[18:20]), int(realData[20:22])) -  Recv.checkDate).days > 0) :
                    serialOut.write(bytes(realData, encoding="utf8"))
                else:
                    DelayStop.DelayStop().start()

            logging.debug(realData)


        if os.path.isfile("run.log") and os.path.getsize("run.log") > (1024*1024*200):
             ShellCmd.execute('echo "" > run.log')

    serialIn.close()


if __name__ == '__main__':
    main(sys.argv[1:])
