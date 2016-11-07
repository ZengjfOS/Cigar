#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import logging
import socket
import fcntl
import struct

def ping(ip):
    if os.system("ping -c 1 " + ip + " > /dev/null") == 0:
        return True
    else:
        logging.error("ping fault.")
        return False

def getMac():
    for line in os.popen("/sbin/ifconfig"):
        if 'ether' in line:
            return line.split()[1]

    return '00:00:00:00:00:00'

def getTimestampe():
    return int(time.time())

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15].encode('utf-8'))
    )[20:24])

