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
from network.Netwok import Network


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


    ser = serial.Serial("/dev/ttymxc2", 57600,
        timeout=1,
        bytesize=serial.EIGHTBITS,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE)

    relayR = 15
    relayStop = 12

    while 1 :

        data = ser.readline()
        if len(data) != 0 and data[0] == 0x02 :

            ser.readline()
            while 1:
                data = ser.readline()
                realData = data.decode().replace('\r\n', '')


                if data[0] == 0x03 :
                    break;
                
                if len(data) == 10 :

                    GPIO.setValue(relayR, 0)
                    GPIO.setValue(relayStop, 0)
                    time.sleep(4)
                    GPIO.setValue(relayR, 1)
                    GPIO.setValue(relayStop, 1)

                    logging.debug(realData)

                if len(data) == 34 :
                    logging.debug(realData)

                if len(data) == 10 or len(data) == 34:

                    if ping(configures.remoteConfig.ip) :
                        Network.connect()
                        Network.sendData(data)
                        Network.disconnect()
                    else :
                        if ping(configures.remoteConfig.ip) :
                            Network.connect()
                            Network.sendData(data)
                            Network.disconnect()
                        else :

                            GPIO.setValue(relayR, 0)
                            GPIO.setValue(relayStop, 0)
                            time.sleep(4)
                            GPIO.setValue(relayR, 1)
                            GPIO.setValue(relayStop, 1)


        if os.path.isfile("run.log") and os.path.getsize("run.log") > (1024*1024*200):
             ShellCmd.execute('echo "" > run.log')

    ser.close()


if __name__ == '__main__':
    main(sys.argv[1:])
