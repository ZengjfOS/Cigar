#/usr/bin/env python
# -*- coding: utf-8 -*-

from network.tools import *
from config.Configures import configures
import threading
from gpio.GPIO import GPIO

class DelayStop(threading.Thread):

    stopCountFlag = 0

    mutex = threading.Lock()

    def run(self):

        relayR = 15
        relayStop = 12

        DelayStop.mutex.acquire()
        DelayStop.stopCountFlag = DelayStop.stopCountFlag + 1
        DelayStop.mutex.release()

        GPIO.setValue(relayR, 0 if configures.localConfig.pindefvalue > 0 else 1)
        GPIO.setValue(relayStop, 0 if configures.localConfig.pindefvalue > 0 else 1)
        time.sleep(1.9)

        DelayStop.mutex.acquire()
        DelayStop.stopCountFlag = DelayStop.stopCountFlag - 1
        DelayStop.mutex.release()

        if (DelayStop.stopCountFlag == 0):
            GPIO.setValue(relayR, configures.localConfig.pindefvalue)
            GPIO.setValue(relayStop, configures.localConfig.pindefvalue)

