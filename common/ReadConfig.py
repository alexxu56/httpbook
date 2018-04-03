# -*- coding: utf-8 -*-
import os
import codecs
import configparser
from  Log import  MyLog as Log

configpath = os.path.split(os.path.realpath(__file__))[0]
inipath = os.path.join(configpath, "config.ini")

class ReadConfig(object):
     def __init__(self):
        fd = open(inipath)
        data = fd.read()
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            file = codecs.open(inipath, 'w')
            file.write(data)
            file.close()
        fd.close()
        self.cf= configparser.ConfigParser()
        self.cf.read(inipath)

     def get_http(self, name):
         value = self.cf.get("HTTP", name)
         return value

     def get_database(self, name):
         value = self.cf.get("DATABASE", name)
         return value
"""
if __name__ == '__main__':
    rc = ReadConfig()
    baseurl = rc.get_http("baseURL")
    print baseurl
"""