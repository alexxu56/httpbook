# -*- coding: utf-8 -*-

import logging
from datetime import datetime
import threading
import os

class Log:
    def __init__(self):
        global logpath, logfilepath, compath
        compath = os.path.abspath(os.path.join(os.path.dirname("__file__"), os.path.pardir))
        logfilepath = os.path.join(compath, "log")
        if not os.path.exists(logfilepath):
            os.mkdir(logfilepath)
        logpath = os.path.join(logfilepath,str(datetime.now().strftime("%Y%m%d%H%M%S")))
        if not os.path.exists(logpath):
            os.mkdir(logpath)
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

        handler = logging.FileHandler(os.path.join(logpath, "output.log"))
        formatter = logging.Formatter('%(asctime)s - %(filename)s:%(name)s - %(levelname)s - %(message)s')

        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def info(self,msg):
        self.logger.info(msg)

    def get_logger(self):
        return  self.logger

class MyLog:
    log = None
    mutex = threading.Lock()
    def __init__(self):
        pass

    @staticmethod
    def get_log():
        if MyLog.log is None:
            MyLog.mutex.acquire()
            MyLog.log = Log()
            MyLog.mutex.release()
        return MyLog.log



