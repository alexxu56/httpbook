# -*- coding: utf-8 -*-
import unittest
import HTMLTestRunner
import os
import time
from common.Log import MyLog as mLog
import common.ReadConfig

#设置日志
#log = mLog.get_log()
#logger = log.get_logger()

#设置路径
runpath = os.path.split(os.path.realpath(__file__))[0]
compath = os.path.abspath(os.path.join(os.path.dirname("__file__"),os.path.pardir))

class TestRun():
    def __init__(self):
        self.caselist = []
        self.caselistfile = os.path.join(runpath,"testlist.txt")
        self.log = mLog.get_log()
        self.logger = self.log.get_logger()
        print self.caselistfile

    def set_case_list(self):
        fb = open(self.caselistfile)
        print fb
        for value in fb.readlines():
            data = str(value)
            print data
            if data != '' and not data.startswith("#"):
                self.caselist.append(data.replace("\n", ""))
        fb.close()

    def set_case_suite(self):
        self.set_case_list()
        test_suite = unittest.TestSuite()
        suite_model = []

        for case in self.caselist:
           # case_file = os.path.join(runpath,"casesrc")
           # print(case_file)
            case_file = runpath
            case_name = case.split("/")[-1]
            print(case_name+".py")
            rundiscover = unittest.defaultTestLoader.discover(case_file,pattern=case_name+".py",top_level_dir=None)
            print rundiscover
            suite_model.append(rundiscover)

#        print len(suite_model)
        if len(suite_model) > 0:
            for suite in suite_model:
                for test_name in suite:
                    test_suite.addTest(test_name)
                    print 9
                    print test_suite
        else:
            return None
        return test_suite

    def run(self):
        try:
            suite = self.set_case_suite()
            print 9
            print suite
            if suite is not None:
                print "test begin"
                self.logger.info("*********Test Start*******")
                now = time.strftime("%Y-%m-%M-%H_%M_%S",time.localtime(time.time()))
                print now
                filepath = os.path.join(compath,"log")
                file = "result" + now + ".html"
                path = os.path.join(filepath,file)
                fp = open(path,'wb')
                runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="Test Report",description= "Test Description")
                runner.run(suite)
        except Exception as ex:
            self.logger.error(str(ex))
        finally:
            self.logger.info("***********TEST END***********")

if __name__ == "__main__":
    testrun = TestRun()
    testrun.run()










