#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 保存对远程MySQL数据库访问的一些参数
class RemoteConfig(object):

    @property
    def ip(self):
        return self._ip

    @ip.setter
    def ip(self, ip):
        self._ip = ip

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, port):
        self._port = port

