# -*- coding: utf-8 -*-

import time
import requests
import ReadConfig as rConfig
from Log import MyLog as Log
from ConnetExcel import ConnectExcelData, exlpath
import json


localreadconfig = rConfig.ReadConfig()

class CallUrl(object):
    def  __init__(self):
        global baseurl,  timeout
        baseurl = localreadconfig.get_http("baseURL")
        timeout = localreadconfig.get_http("timeout")
        self.log = Log.get_log()
        self.logger = self.log.get_logger()
        self.headers = {}
        self.params = {}
        self.data = {}
        self.url = None
        self.files = {}
        self.requestresult = {}

    def set_url(self,interface):
         self.url = baseurl + interface

    def set_headers(self,header):
         self.headers = header

    def set_params(self, param):
        self.params = param

    def set_data(self, data):
        self.data = data

    def set_files(self, file):
        self.filse = file

    def get_url(self):
         try:
             response = requests.get(self.url, params= self.params, headers= self.headers, timeout= float(timeout))
             return response
         except RuntimeError:
             self.logger.error("Time out!")
             return  None

    def post_url(self):
         try:
             response = requests.post(self.url, params= self.params, headers= self.headers, timeout= float(timeout))
             return response
         except RuntimeError:
             self.logger.error("Time out!")
             return  None

    def get_serviceurl(self, sericeurl, serviceparams):
        timebefore = time.time()
        try:
            response = requests.get(sericeurl, params=serviceparams, timeout=float(timeout))
            timeend = time.time()
            tmpjson = response.json()
            self.requestresult['rjson'] = tmpjson
            self.requestresult['rtime'] = round(timeend - timebefore, 2)
            return self.requestresult
        except RuntimeError:
             self.logger.error("Time out!")
             return  None

    def post_serviceurl(self, sericeurl, serviceparams):
         timebefore = time.time()
         try:
             response = requests.post(sericeurl, data=serviceparams, timeout=float(timeout))
             timeend = time.time()
             tmpjson = response.json()
             self.requestresult['rjson'] = tmpjson
             self.requestresult['rtime'] = round(timeend-timebefore,2)
             return self.requestresult
         except RuntimeError:
             self.logger.error("Time out!")
             return  None

"""
if __name__ == '__main__':
    filename = 'caseData.xlsx'
    begincase = '00001'
    casenum = 1
    conxls = ConnectExcelData(filename, exlpath)
    caselist = conxls.get_case_List(conxls.absFile, begincase, casenum)
    callurl = CallUrl()
    for casedict in caselist:
        caseid = casedict['id']
        print caseid
        caseintf = casedict['interface']
        print caseintf
        baseurl = localreadconfig.get_http("baseURL")
        serviceurl= baseurl+ caseintf
        print serviceurl
        serviceparams = {}
        resp = callurl.post_serviceurl(serviceurl, serviceparams)
#        resp = callurl.get_serviceurl(serviceurl, serviceparams)
        tmjson = resp.json()
        tbook = tmjson['root']
        print tmjson['totalProperty']
        print tbook

        ttbook = tbook[0]
        print tbook[1]['author']
"""





