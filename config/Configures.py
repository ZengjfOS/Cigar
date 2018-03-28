#!/usr/bin/env python
# -*- coding: utf-8 -*-

import configparser

from logging import *
from config.LocalConfig import LocalConfig
from config.RemoteConfig import RemoteConfig

# 初始化配置
class Configures(object):

    # 使用单例模式来生成统一的对象
    def __new__(cls, *args, **kwargs):

        if not hasattr(cls, "_inst"):

            # 单例对象
            cls._inst = super(Configures, cls).__new__(cls)

            # 生成两个内部对象
            cls.localConfig = LocalConfig()
            cls.remoteConfig = RemoteConfig()

            # 配置并解析配置文件
            config = configparser.ConfigParser()
            config.read("config.conf")

            # 获取远程网络参数
            remoteTag = "remote"
            cls.remoteConfig.ip = config.get(remoteTag, "IP")
            cls.remoteConfig.port = config.getint(remoteTag, "Port")

            # 获取本地配置参数
            localTag = "localhost"
            cls.localConfig.debug = config.getboolean(localTag, "Debug")
            cls.localConfig.scanUart = config.get(localTag, "ScanUart")
            cls.localConfig.scanBaudrate = config.get(localTag, "ScanBaudrate")
            cls.localConfig.pindefvalue = config.getint(localTag, "PinDefValue")

            # 设置log等级
            infoLevel = DEBUG
            if not cls.localConfig.debug:
                infoLevel = ERROR

            if not config.getboolean(localTag, "Console"):
                basicConfig(level=infoLevel,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=config.get(localTag, "logFileName"),
                    filemode='a'
                )
            else:
                basicConfig(level=infoLevel,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                )


            debug("[Debug configure data]:")
            debug("\tlocalhost Debug: %s" % cls.localConfig.debug)

            debug("[Remote configure data]:")
            debug("\tremote IP: %s" % cls.remoteConfig.ip)
            debug("\tremote Port: %d" % cls.remoteConfig.port)

            debug("[Local configure data]:")
            debug("\tlocal ScanUart: %s" % cls.localConfig.scanUart)
            debug("\tlocal ScanBaudrate: %s" % cls.localConfig.scanBaudrate)

        return cls._inst

configures = Configures()

if __name__ == '__main__':

    # 输出信息：
    #     < __main__.Configures object at 0x7f7404fb3240 >
    #     < __main__.Configures object at 0x7f7404fb3240 >
    #     < __main__.Configures object at 0x7f7404fb3240 >
    debug(Configures())
    debug(Configures())
    debug(configures)
