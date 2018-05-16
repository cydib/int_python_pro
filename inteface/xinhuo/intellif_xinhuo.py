#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-27 14:14:20
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import requests
import json
import base64
import os
import MySQLdb
import urllib.request
import xlrd
import xlwt
import time

### Setting ###########################

tokenlist = {"password": "81dc9bdb52d04dc20036dbd8313ed055", "username": "yinyi",
             "grant_type": "password", "scope": "read write", "client_secret": 123456, "client_id": "clientapp"}


### Setting ###########################


class Test:

    def __init__(self):
        self.base_url = "http://172.18.224.160:8082/api/intellif/xinghuo/faceRecog/faceApp/"
        self.s = requests.Session()
        self.headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                        "Authorization": "Basic Y2xpZW50YXBwOjEyMzQ1Ng=="}

    def getToken(self):
        r = self.s.post("http://172.18.224.160:8082/api/oauth/token",
                        data=tokenlist, headers=self.headers)
        r.connection.close()
        # print(r.text)
        token = json.loads(r.text)["access_token"]
        return "Bearer " + token

    def now(self):
        return time.strftime("%Y-%m-%d_%H-%M-%S"), time.strftime("%Y-%m-%d %H:%M:%S")

    def upLoadimg(self, img):
        with open(img, "rb") as f:
            base64_img = base64.b64encode(f.read())
            baseimg = str(base64_img).split("'")[1]
            r = self.s.post(self.base_url + "ytUpload", data=json.dumps(
                {"FacePic": baseimg, "OrgPic": baseimg, "password_key": "b6a03412", "username": "ytlf"}), headers={
                "Content-Type": "application/json;charset=UTF-8", "Authorization": self.getToken()})
            r.connection.close()
            # print(r.text)
            time.sleep(1)

            try:
                guid = json.loads(r.text)
                return guid["guid"]
            except:
                # print(json.loads(r.text)['message'])
                print(r.text)
                return "error"

    def ytFaces(self):

        workbook = xlwt.Workbook(encoding='ascii')
        worksheet = workbook.add_sheet("test_result")

        tableheader = {0: "图像", 1: "依图", 2: "优图",
                       3: "商汤", 4: "Face++", 5: "云天励飞"}
        for col, cname in tableheader.items():
            worksheet.write(0, col, label=cname)

        row1 = 0  # 图像行
        num = 0
        for oriimg in os.listdir("./samples"):
            row1 += 1
            num += 1
            worksheet.write(row1, 0, label=oriimg)
            guid1 = self.upLoadimg("./samples/" + oriimg)
            print("样本 %s ：%s" % (num, oriimg))

            for PlatformID in range(3, 9):
                if PlatformID == 3:
                    print(self.now()[1] + "【 依图 】：", end='')
                elif PlatformID == 4:
                    print(self.now()[1] + "【 优图 】：", end='')
                elif PlatformID == 5:
                    print(self.now()[1] + "【 商汤 】：", end='')
                elif PlatformID == 6:
                    print(self.now()[1] + "【Face++】：", end='')
                elif PlatformID == 7:
                    continue
                elif PlatformID == 8:
                    print(self.now()[1] + "【 云天 】：", end='')

                ytpayload = {"guid": guid1, "PlatformID": PlatformID, "DataSource": "1,2,3,4,5,6,7,8,9,10",
                             "TopPic": "30",
                             "TimeOut": "15", "UserID": "ytlf", "source": "ytlf", "AgeGroup": "", "AreaCode": "",
                             "SEX": ""}
                r = self.s.post(self.base_url + "ytFaces", data=json.dumps(ytpayload), headers={
                    "Content-Type": "application/json;charset=UTF-8", "Authorization": self.getToken()})
                r.connection.close()
                time.sleep(1)

                reason = ''
                for top in range(0, 30):
                    try:
                        topPicNo = json.loads(
                            r.text)["memberlist"][top]["topPicNo"]

                        result = json.loads(
                            r.text)["memberlist"][top]["idCard"]
                    except:
                        try:
                            reason = json.loads(r.text)["message"]
                            result = ''
                        except:
                            try:
                                reason = json.loads(r.text)["data"]
                                result = ''
                            except:
                                reason = "接口出错"
                                result = ''

                    if (result == oriimg.split("_")[1].split(".")[0]):

                        if PlatformID == 3:
                            print("识别正确，排名 TOP：%s" % topPicNo)
                            worksheet.write(row1, 1, label=topPicNo)
                        elif PlatformID == 4:
                            print("识别正确，排名 TOP：%s" % topPicNo)
                            worksheet.write(row1, 2, label=topPicNo)
                        elif PlatformID == 5:
                            print("识别正确，排名 TOP：%s" % topPicNo)
                            worksheet.write(row1, 3, label=topPicNo)
                        elif PlatformID == 6:
                            print("识别正确，排名 TOP：%s" % topPicNo)
                            worksheet.write(row1, 4, label=topPicNo)
                        elif PlatformID == 8:
                            print("识别正确，排名 TOP：%s" % topPicNo)
                            worksheet.write(row1, 5, label=topPicNo)
                        break

                else:
                    if PlatformID == 3:
                        if not reason:
                            print("识别错误")
                            worksheet.write(row1, 1, label="识别错误")
                        else:
                            print(reason)
                            worksheet.write(row1, 1, label=reason)
                    elif PlatformID == 4:
                        if not reason:
                            print("识别错误")
                            worksheet.write(row1, 2, label="识别错误")
                        else:
                            print(reason)
                            worksheet.write(row1, 2, label=reason)
                    elif PlatformID == 5:
                        if not reason:
                            print("识别错误")
                            worksheet.write(row1, 3, label="识别错误")
                        else:
                            print(reason)
                            worksheet.write(row1, 3, label=reason)
                    elif PlatformID == 6:
                        if not reason:
                            print("识别错误")
                            worksheet.write(row1, 4, label="识别错误")
                        else:
                            print(reason)
                            worksheet.write(row1, 4, label=reason)
                    elif PlatformID == 8:
                        if not reason:
                            print("识别错误")
                            worksheet.write(row1, 5, label="识别错误")
                        else:
                            print(reason)
                            worksheet.write(row1, 5, label=reason)

        excelname = self.now()[0]
        workbook.save(excelname + "_result.xls")
        print("\n")
        print("对比结束，请查看对比结果文件：%s" % (excelname + "_result.xls"))


if __name__ == '__main__':
    Test().ytFaces()
