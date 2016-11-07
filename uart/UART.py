#!/usr/bin/env python
# -*- coding: utf-8 -*-

import serial

class UART(object):

    curSerial = serial.Serial()

    @staticmethod
    def openPort(port, baudrate,
                         timeoutArg=1,
                         bytesizeArg=serial.EIGHTBITS,
                         parityArg=serial.PARITY_NONE,
                         stopbitsArg=serial.STOPBITS_ONE):
        UART.curSerial =  serial.Serial(port, baudrate,
                             timeout=timeoutArg,
                             bytesize=bytesizeArg,
                             parity=parityArg,
                             stopbits=stopbitsArg)

    @staticmethod
    def readByte(count=1):
        if UART.curSerial.is_open :
            return UART.readByte(count)

    @staticmethod
    def readLine():
        if UART.curSerial.is_open :
            return UART.readLine()

    @staticmethod
    def close():
        if UART.curSerial.is_open :
            UART.curSerial.close()
