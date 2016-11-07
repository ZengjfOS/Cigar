#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 保存对本地设置的一些配置参数
class LocalConfig(object):

    @property
    def debug(self):
        return self._debug

    @debug.setter
    def debug(self, debug):
        self._debug = debug

    @property
    def scanUart(self):
        return self._scanUart

    @scanUart.setter
    def scanUart(self, scanUart):
        self._scanUart = scanUart

    @property
    def scanBaudrate(self):
        return self._scanBaudrate

    @scanBaudrate.setter
    def scanBaudrate(self, scanBaudrate):
        self._scanBaudrate = scanBaudrate
