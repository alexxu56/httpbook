# -*- coding: utf-8 -*-
import common.ReadConfig as rConfig
from common.ConnetExcel import ConnectExcelData, exlpath
from common.CallHttp import CallUrl
import unittest

class testgetBookList(unittest.TestCase):
    def testgetbooklist(self):
        #设置基本参数
        filename = 'caseData.xlsx'
        begincase = '00003'
        casenum = 1
        #获取案例数据
        conxls = ConnectExcelData(filename, exlpath)
        caselist = conxls.get_case_List(conxls.absFile, begincase, casenum)
        print caselist
        #对于每一个案例调用接口
        for casedict in caselist:
            caseid = casedict['id']
            print caseid
            caseintf = casedict['interface']
 #           print caseintf
            localreadconfig = rConfig.ReadConfig()
            baseurl = localreadconfig.get_http("baseURL")
            serviceurl = baseurl + caseintf
 #          print serviceurl
            serviceparams = {}
            respdict = {}
            callurl = CallUrl()
            respdict = callurl.get_serviceurl(serviceurl, serviceparams)

            tmpjson = respdict['rjson']
            restime = respdict['rtime']
            print tmpjson
#            resjson = tmpjson['root'][0]
#            print resjson
            resjson = tmpjson['error']
#           booknum = tmpjson['totalProperty']
            booknum = 0
#            print tmpjson.keys()
#           print tbook[1]['author']
            rescode = tmpjson['status']
            therow = conxls.get_row_num(conxls.absFile, 'dataout', caseid)
            print therow
            conxls.write_case_result(resjson, restime, booknum, rescode, conxls.absFile, therow+1)

#if __name__ == '__main__':
#    booklist = GetBookList()
#    booklist.get_book_list()
