# -*- coding: utf-8 -*-
import common.ReadConfig as rConfig
from common.ConnetExcel import ConnectExcelData, exlpath
from common.CallHttp import CallUrl

class GetBookList(object):
    def __init__(self):
        pass

    def get_book_list(self,filename, begincase, casenum, bookid):
        #获取案例数据
        conxls = ConnectExcelData(filename, exlpath)
        caselist = conxls.get_case_List(conxls.absFile, begincase, casenum)

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
            respdict = callurl.post_serviceurl(serviceurl, serviceparams)
            tmpjson = respdict['rjson']
            restime = respdict['rtime']
#            resjson = tmpjson['root'][0]
#            print resjson
#            for bid in resjson
#            tbook[1]['author']
            resjson = 0
            print tmpjson
            booknum = tmpjson['totalProperty']
#            print tmpjson.keys()
#           print tbook[1]['author']
            rescode = 0
            therow = conxls.get_row_num(conxls.absFile, 'dataout', caseid)
            print therow
            conxls.write_case_result(resjson, restime, booknum, rescode, conxls.absFile, therow+1)
            if bookid > 0 and int(booknum) > 0:
                books = tmpjson['root']
                for book in books:
                    if int(book['id']) == int(bookid):
                        print book['id']
                        conxls.write_book_result(book, conxls.absFile, therow+1)


                #    if int(books[n-1]['id']) == int(bookid):
                #        print books[n-1]['id']
 #              #         qbooklist.append(book)
#    continue
