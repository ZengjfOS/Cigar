#!/usr/bin/env python
# -*- coding: utf-8 -*-

import getopt
import logging
import os
import sys
import time
import serial
import re

from gpio.GPIO import GPIO
from shell.ShellCmd import ShellCmd
from network.tools import *
from config.Configures import configures
from network.Netwok import Network
from DelayStop import DelayStop


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


    ser = serial.Serial("/dev/ttymxc2", 9600,
        timeout=1,
        bytesize=serial.EIGHTBITS,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE)

    printPort = serial.Serial("/dev/ttymxc1", 9600,
                        timeout=1,
                        bytesize=serial.EIGHTBITS,
                        parity=serial.PARITY_NONE,
                        stopbits=serial.STOPBITS_ONE)

    relayR = 15
    relayStop = 12

    GPIO.initGPIOOut(12, configures.pindefvalue)
    GPIO.initGPIOOut(15, configures.pindefvalue)

    while 1 :

        data = ser.readline()

        if len(data) <= 0 :
            continue

        if ((re.search(r"NoRead\r\n", data.decode()) != None) and (len(data) == 8)) or ((re.search(r"\d{32}\r\n", data.decode()) != None) and (len(data) == 34)):

            # 复位控制信号
            GPIO.setValue(relayR, configures.pindefvalue)
            GPIO.setValue(relayStop, configures.pindefvalue)

            realData = data.decode().replace('\r\n', '')

            # if (ping(configures.remoteConfig.ip)):
            network = Network()
            network.setData(realData)
            network.setSerial(printPort)
            network.start()

            if (re.search(r"NoRead\r\n", data.decode()) != None) and (len(data) == 8):

                DelayStop().start()
                logging.debug(realData)

            if (re.search(r"\d{32}\r\n", data.decode()) != None) and (len(data) == 34):
                logging.debug(realData)


        if os.path.isfile("run.log") and os.path.getsize("run.log") > (1024*1024*200):
             ShellCmd.execute('echo "" > run.log')

    ser.close()
    printPort.close()


if __name__ == '__main__':
    main(sys.argv[1:])
