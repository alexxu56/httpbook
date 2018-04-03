# -*- coding: utf-8 -*-
from getBookList import GetBookList
import unittest
from common.Log import MyLog as mLog
#设置日志
log = mLog.get_log()
logger = log.get_logger()

class getBookList(unittest.TestCase):
    def testgetbook(self):
        filename = 'caseData.xlsx'
        begincase = '00001'
        casenum = 2
        inbookid = 0
        booklist = GetBookList()
        logger.info("*********Test Start*******")
        booklist.get_book_list(filename, begincase, casenum, inbookid)

#if __name__ == '__main__':
#    # 设置基本参数


