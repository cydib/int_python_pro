#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-08 11:44:10
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
import requests
import json


class GetHouse:
    def __init__(self):
        self.base_url = "http://www.cszjw.net/"
        self.data1 = {"area": "cs", "idcard": "43092319880305381x",
                      "_token": "3L29SwFbeVsKOcUSkXSweoy07qeGaxd9XIsXajd86", "htbh": "xx1701932406", "verify_code": "zz63"}
        self.s = requests.Session()
        self.headers = {"Accept": "application/json, text/javascript, */*; q=0.01",
                        "Accept-Encoding": "gzip, deflate",
                        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7",
                        "Cache-Control": "no-cache",
                        "Connection": "keep-alive",
                        "Content-Length": "116",
                        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                        "Cookie": "XSRF-TOKEN=eyJpdiI6IkM0clZDTzZrT1RiODRtWE0ySThQM3c9PSIsInZhbHVlIjoiaWlEalo4c1wvSGFPRjhwYWhZMWlyTm9mVTJHSE16RFwvT25aN2VITnhFaXNMbU5Gb1hwaGpnOXBPa1ZNbDZXaDdaOUcyWEtEdmhEUTN4VmdRd0g5bXkrZz09IiwibWFjIjoiNzYzYjQ0OTE3MjIxZWZiODZiN2RiMTc0OTUwZjliZGQzNDcxMjhjY2ExYWIyODJlZGJmZTFiNjkxODI4ZGE4OCJ9; laravel_session=eyJpdiI6InFCdlh1UDRVTWlNZXpWb3hMb0tzNFE9PSIsInZhbHVlIjoib0JBaDNURnNoUEVtVWpGUWpKU21BTTFQV2RzaUlkVjQ0UjUxZkNrTXdnUEFnNVdydG95VEJxVkxrMGhjSXZjMkZLNUl5Y1N2VTQ4QnJyOXhRRlR4a3c9PSIsIm1hYyI6IjBhZDg0OTc5NDU0MTcyZjJjNjNmMzYxYTE3NWZkMmE0YzNmNjVkOTE1YTgwMDM2NDdkMzM4ODJlY2NiMWU5NGUifQ%3D%3D",
                        "Host": "www.cszjw.net",
                        "Origin": "http://www.cszjw.net",
                        "Pragma": "no-cache",
                        "Referer": "http://www.cszjw.net/signedcontract",
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
                        "X-Requested-With": "XMLHttpRequest"}
        self.cookies = {"XSRF-TOKEN": "eyJpdiI6IkM0clZDTzZrT1RiODRtWE0ySThQM3c9PSIsInZhbHVlIjoiaWlEalo4c1wvSGFPRjhwYWhZMWlyTm9mVTJHSE16RFwvT25aN2VITnhFaXNMbU5Gb1hwaGpnOXBPa1ZNbDZXaDdaOUcyWEtEdmhEUTN4VmdRd0g5bXkrZz09IiwibWFjIjoiNzYzYjQ0OTE3MjIxZWZiODZiN2RiMTc0OTUwZjliZGQzNDcxMjhjY2ExYWIyODJlZGJmZTFiNjkxODI4ZGE4OCJ9",
                        "laravel_session": "eyJpdiI6InFCdlh1UDRVTWlNZXpWb3hMb0tzNFE9PSIsInZhbHVlIjoib0JBaDNURnNoUEVtVWpGUWpKU21BTTFQV2RzaUlkVjQ0UjUxZkNrTXdnUEFnNVdydG95VEJxVkxrMGhjSXZjMkZLNUl5Y1N2VTQ4QnJyOXhRRlR4a3c9PSIsIm1hYyI6IjBhZDg0OTc5NDU0MTcyZjJjNjNmMzYxYTE3NWZkMmE0YzNmNjVkOTE1YTgwMDM2NDdkMzM4ODJlY2NiMWU5NGUifQ%3D%3D"}

    def getverifycode(self):
        r = requests.get(self.base_url+"newCaptcha")
        r.encoding = 'GBK'
        print(r.text)

    def signedcontract(self):
        r = self.s.post(self.base_url+"signedcontract",
                        data=json.dumps(self.data1), headers=self.headers, cookies=self.cookies)
        r.encoding = 'utf-8'
        print(r, r.text)


    def signedcontract1(self):
    	r = self.s.post("http://www.cszjw.net/registration",data=self.data1,headers=self.headers,cookies=self.cookies)
    	r.encoding = 'utf-8'
    	print(r.text)

if __name__ == '__main__':
    GetHouse().signedcontract1()
