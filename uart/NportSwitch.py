#/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import time
import logging

class NportSwitch(threading.Thread):

    nportInPort = None;
    sickOutPort = None;

    @staticmethod
    def setNportInPort(inSerial):
        NportSwitch.nportInPort = inSerial

    @staticmethod
    def setSickOutPort(outSerial):
        NportSwitch.sickOutPort = outSerial

    def run(self):

        while True :

            try:
                if(NportSwitch.nportInPort == None or NportSwitch.sickOutPort == None) :
                    pass
                else :
                    back_str = NportSwitch.nportInPort.read(128)
                    if (back_str == None or len(back_str) == 0) :
                        continue
                    NportSwitch.sickOutPort.write(back_str)

                time.sleep(1)
            except :
                logging.debug("NportSwitch data except. ")

if __name__ == '__main__':
    NportSwitch().start();
    time.sleep(2)
    NportSwitch.setNportInPort("zengjf")
    NportSwitch.setSickOutPort("zengjf")
