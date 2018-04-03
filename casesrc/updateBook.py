# -*- coding: utf-8 -*-
import common.ReadConfig as rConfig
import json
from common.ConnetExcel import ConnectExcelData, exlpath
from common.CallHttp import CallUrl

class UpdateBook(object):
    def __init__(self):
        pass

    def update_book(self, filename, begincase, casenum):
        booklist = []
        #获取案例数据
        conxls = ConnectExcelData(filename, exlpath)
        caselist = conxls.get_case_List(conxls.absFile, begincase, casenum)

        # 对于每一个案例调用接口
        for casedict in caselist:
            caseid = casedict['id']
            print caseid
            caseintf = casedict['interface']
            #            print caseintf
            datadict = {}
            datadict['id'] = str(int(casedict['bookid']))
            datadict['name'] = casedict['bookname']
            datadict['author'] = casedict['bookauthor']
            datadict['year'] = str(int(casedict['bookyear']))
            datadict['digest'] = casedict['bookdigest']
            datadict['caseid'] = caseid
            booklist.append(datadict)
            print datadict
            serviceparams = {}

            # 给接口赋值，bookValues json格式
            serviceparams['bookValues'] = json.dumps(datadict)
            localreadconfig = rConfig.ReadConfig()
            baseurl = localreadconfig.get_http("baseURL")
            serviceurl = baseurl + caseintf
            print serviceurl

            callurl = CallUrl()
            respdict = callurl.post_serviceurl(serviceurl, serviceparams)
            tmpjson = respdict['rjson']
            restime = respdict['rtime']
            print tmpjson
            #            print tmpjson['error']
            #
            success1 = tmpjson['success']
            errorNo1 = tmpjson['errorNo']
            errorInfo1 = tmpjson['errorInfo']
            print tmpjson['success']
            print tmpjson['errorNo']
            print tmpjson['errorInfo']
            therow = conxls.get_row_num(conxls.absFile, 'dataout', caseid)
            print therow
            conxls.write_case_result(errorInfo1, restime, success1, errorNo1, conxls.absFile, therow + 1)
        return booklist
"""
if __name__ == '__main__':
    # addbook
    filename = 'caseUpdate.xlsx'
    begincase = '00301'
    casenum = 2

    updatebooklist = UpdateBook()
    booklist = updatebooklist.update_book(filename, begincase, casenum)
"""