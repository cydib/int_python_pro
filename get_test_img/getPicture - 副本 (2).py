#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-26 11:14:20
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$
# 运行前先请先安装python3第三方库:pip install mysqlclient

import os, MySQLdb, urllib.request, json

class GetImg():

    def __init__(self,ip, port, username, password, database):
        self.db = MySQLdb.connect(host=ip, port=port, user=username, passwd=password, db=database, charset="utf8")



    def createDir(self):
        os.makedirs("./gender/female/confid_less_0.8", exist_ok=True)
        os.makedirs("./gender/female/confid_more_0.8", exist_ok=True)
        os.makedirs("./gender/male/confid_more_0.8", exist_ok=True)
        os.makedirs("./gender/male/confid_less_0.8", exist_ok=True)
        os.makedirs("./gender/unknow/confid_less_0.8", exist_ok=True)
        os.makedirs("./gender/unknow/confid_more_0.8", exist_ok=True)

        os.makedirs("./race/han/confid_less_0.8", exist_ok=True)
        os.makedirs("./race/han/confid_more_0.8", exist_ok=True)
        os.makedirs("./race/other/confid_more_0.8", exist_ok=True)
        os.makedirs("./race/other/confid_less_0.8", exist_ok=True)

        os.makedirs("./glasses/unknow/confid_less_0.8", exist_ok=True)
        os.makedirs("./glasses/unknow/confid_more_0.8", exist_ok=True)
        os.makedirs("./glasses/No_glasses/confid_less_0.8", exist_ok=True)
        os.makedirs("./glasses/No_glasses/confid_more_0.8", exist_ok=True)
        os.makedirs("./glasses/Ordinary_glasses/confid_less_0.8", exist_ok=True)
        os.makedirs("./glasses/Ordinary_glasses/confid_more_0.8", exist_ok=True)
        os.makedirs("./glasses/sunglasses/confid_less_0.8", exist_ok=True)
        os.makedirs("./glasses/sunglasses/confid_more_0.8", exist_ok=True)

        for i in range(0, 10):
            os.makedirs("./age/%s" % i, exist_ok=True)


        os.makedirs("./hat/have_hat/confid_less_0.8", exist_ok=True)
        os.makedirs("./hat/have_hat/confid_more_0.8", exist_ok=True)
        os.makedirs("./hat/no_hat/confid_more_0.8", exist_ok=True)
        os.makedirs("./hat/no_hat/confid_less_0.8", exist_ok=True)
        os.makedirs("./hat/unknow/confid_more_0.8", exist_ok=True)
        os.makedirs("./hat/unknow/confid_less_0.8", exist_ok=True)





    def getGender(self):
        db = connsql("192.168.11.128", 3306, "root", 'introcks1234', "intellif_face")
        sql = "SELECT (gender & 15) AS gender1, f.image_data,f.json FROM intellif_face.t_face_24 f where ((gender & 112) / 16) <= 5 ORDER BY TIME DESC;"
        cursor = db.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        num = 0
        for i in data:
            num += 1
            gender = i[0]
            img_url = i[1]
            try:
                geconfid = json.loads(i[2])["Confidence"]['Gender']
            except:
                continue
            glconfid = json.loads(i[2])["Confidence"]['Glass']
            hconfid = json.loads(i[2])["Confidence"]['Hat']
            rconfid = json.loads(i[2])["Confidence"]['Race']

            print("性别样本采集...第" + str(num) + "张", gender, img_url, geconfid, glconfid, hconfid, rconfid)
            if gender == 2 and geconfid <= 0.83:
                urllib.request.urlretrieve(img_url,
                                           "./gender/female/confid_less_0.8\\%s" % str(
                                               "gender_" + str(gender) + "_gconfid_" + str(geconfid) + "_" + str(num)+".jpg"))
            elif gender == 2 and geconfid > 0.83:
                urllib.request.urlretrieve(img_url,
                                           "./gender/female/confid_more_0.8\\%s" % str(
                                               "gender_" + str(gender) + "_gconfid_" + str(geconfid) + "_" + str(num)+".jpg"))
            elif gender == 1 and geconfid <= 0.83:
                urllib.request.urlretrieve(img_url,
                                           "./gender/male/confid_less_0.8\\%s" % str(
                                               "gender_" + str(gender) + "_gconfid_" + str(geconfid) + "_" + str(num)+".jpg"))
            elif gender == 1 and geconfid > 0.83:
                urllib.request.urlretrieve(img_url,
                                           "./gender/male/confid_more_0.8\\%s" % str(
                                               "gender_" + str(gender) + "_gconfid_" + str(geconfid) + "_" + str(num)+".jpg"))
            elif gender == 0 and geconfid <= 0.83:
                urllib.request.urlretrieve(img_url,
                                           "./gender/unknow/confid_less_0.8\\%s" % str(
                                               "gender_" + str(gender) + "_gconfid_" + str(geconfid) + "_" + str(num)+".jpg"))
            elif gender == 0 and geconfid > 0.83:
                urllib.request.urlretrieve(img_url,
                                           "./gender/unknow/confid_more_0.8\\%s" % str(
                                               "gender_" + str(gender) + "_gconfid_" + str(geconfid) + "_" + str(num)+".jpg"))


    def getrace(self):
        db = connsql("192.168.11.128", 3306, "root", 'introcks1234', "intellif_face")
        sql = "SELECT (race & 15) AS race1,f.image_data,f.json FROM intellif_face.t_face_24 f where ((race & 112) / 16) <= 5 ORDER BY TIME DESC;"
        cursor = db.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        num = 0
        for i in data:
            num += 1
            race = i[0]
            img_url = i[1]
            try:
                geconfid = json.loads(i[2])["Confidence"]['Gender']
            except:
                continue
            glconfid = json.loads(i[2])["Confidence"]['Glass']
            hconfid = json.loads(i[2])["Confidence"]['Hat']
            rconfid = json.loads(i[2])["Confidence"]['Race']

            print("种族样本采集...第" + str(num) + "张", race, img_url, geconfid, glconfid, hconfid, rconfid)
            if race == 0 and rconfid <= 0.83:
                urllib.request.urlretrieve(img_url,
                                           "./race/han/confid_less_0.8\\%s" % str(
                                               "race_" + str(race) + "_rconfid_" + str(rconfid) + "_" + str(num)+".jpg"))
            elif race == 0 and rconfid > 0.83:
                urllib.request.urlretrieve(img_url,
                                           "./race/han/confid_more_0.8\\%s" % str(
                                               "race_" + str(race) + "_rconfid_" + str(rconfid) + "_" + str(num)+".jpg"))
            elif race == 1 and rconfid <= 0.83:
                urllib.request.urlretrieve(img_url,
                                           "./race/other/confid_less_0.8\\%s" % str(
                                               "race_" + str(race) + "_rconfid_" + str(rconfid) + "_" + str(num)+".jpg"))
            elif race == 1 and rconfid > 0.83:
                urllib.request.urlretrieve(img_url,
                                           "./race/other/confid_more_0.8\\%s" % str(
                                               "race_" + str(race) + "_rconfid_" + str(rconfid) + "_" + str(num)+".jpg"))


    def getglasses(self):
        db = connsql("192.168.11.128", 3306, "root", 'introcks1234', "intellif_face")
        sql = "SELECT (accessories & 15) AS glasses1,f.image_data,f.json FROM intellif_face.t_face_24 f where ((accessories & 112) / 16) <= 5 ORDER BY TIME DESC;"
        cursor = db.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        num = 0
        for i in data:
            num += 1
            glasses = i[0]
            img_url = i[1]
            try:
                geconfid = json.loads(i[2])["Confidence"]['Gender']
            except:
                continue
            glconfid = json.loads(i[2])["Confidence"]['Glass']
            hconfid = json.loads(i[2])["Confidence"]['Hat']
            rconfid = json.loads(i[2])["Confidence"]['Race']

            print("眼镜样本采集...第" + str(num) + "张", glasses, img_url, geconfid, glconfid, hconfid, rconfid)
            if glasses == 0 and glconfid <= 0.83:
                urllib.request.urlretrieve(img_url,
                                           "./glasses/unknow/confid_less_0.8\\%s" % str(
                                               "glasses_" + str(glasses) + "_glconfid_" + str(glconfid) + "_" + str(num)+".jpg"))
            elif glasses == 0 and glconfid > 0.83:
                urllib.request.urlretrieve(img_url,
                                           "./glasses/unknow/confid_more_0.8\\%s" % str(
                                               "glasses_" + str(glasses) + "_glconfid_" + str(glconfid) + "_" + str(num)+".jpg"))
            elif glasses == 1 and glconfid <= 0.83:
                urllib.request.urlretrieve(img_url,
                                           "./glasses/No_glasses/confid_less_0.8\\%s" % str(
                                               "glasses_" + str(glasses) + "_glconfid_" + str(glconfid) + "_" + str(num)+".jpg"))
            elif glasses == 1 and glconfid > 0.83:
                urllib.request.urlretrieve(img_url,
                                           "./glasses/No_glasses/confid_more_0.8\\%s" % str(
                                               "glasses_" + str(glasses) + "_glconfid_" + str(glconfid) + "_" + str(num)+".jpg"))
            elif glasses == 2 and glconfid <= 0.83:
                urllib.request.urlretrieve(img_url,
                                           "./glasses/Ordinary_glasses/confid_less_0.8\\%s" % str(
                                               "glasses_" + str(glasses) + "_glconfid_" + str(glconfid) + "_" + str(num)+".jpg"))
            elif glasses == 2 and glconfid > 0.83:
                urllib.request.urlretrieve(img_url,
                                           "./glasses/Ordinary_glasses/confid_more_0.8\\%s" % str(
                                               "glasses_" + str(glasses) + "_glconfid_" + str(glconfid) + "_" + str(num)+".jpg"))
            elif glasses == 3 and glconfid <= 0.83:
                urllib.request.urlretrieve(img_url,
                                           "./glasses/sunglasses/confid_less_0.8\\%s" % str(
                                               "glasses_" + str(glasses) + "_glconfid_" + str(glconfid) + "_" + str(num)+".jpg"))
            elif glasses == 3 and glconfid > 0.83:
                urllib.request.urlretrieve(img_url,
                                           "./glasses/sunglasses/confid_more_0.8\\%s" % str(
                                               "glasses_" + str(glasses) + "_glconfid_" + str(glconfid) + "_" + str(num)+".jpg"))


    def gethat(self):
        db = connsql("192.168.11.128", 3306, "root", 'introcks1234', "intellif_face")
        sql = "SELECT (accessories & 3840) / 256 AS hat1, f.image_data,f.json FROM intellif_face.t_face_24 f where ((accessories & 28672) / 4096) <= 5 ORDER BY TIME DESC;"
        cursor = db.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        num = 0
        for i in data:
            num += 1
            hat = i[0]
            img_url = i[1]
            try:
                geconfid = json.loads(i[2])["Confidence"]['Gender']
            except:
                continue
            glconfid = json.loads(i[2])["Confidence"]['Glass']
            hconfid = json.loads(i[2])["Confidence"]['Hat']
            rconfid = json.loads(i[2])["Confidence"]['Race']

            print("帽子样本采集...第" + str(num) + "张", hat, img_url, geconfid, glconfid, hconfid, rconfid)
            if hat == 0 and hconfid <= 0.83:
                urllib.request.urlretrieve(img_url,
                                           "./hat/unknow/confid_less_0.8\\%s" % str(
                                               "hat_" + str(hat) + "_hconfid_" + str(hconfid) + "_" + str(num)+".jpg"))
            elif hat == 0 and hconfid > 0.83:
                urllib.request.urlretrieve(img_url,
                                           "./hat/unknow/confid_more_0.8\\%s" % str(
                                               "hat_" + str(hat) + "_hconfid_" + str(hconfid) + "_" + str(num)+".jpg"))
            elif hat == 1 and hconfid <= 0.83:
                urllib.request.urlretrieve(img_url,
                                           "./hat/no_hat/confid_less_0.8\\%s" % str(
                                               "hat_" + str(hat) + "_hconfid_" + str(hconfid) + "_" + str(num)+".jpg"))
            elif hat == 1 and hconfid > 0.83:
                urllib.request.urlretrieve(img_url,
                                           "./hat/no_hat/confid_more_0.8\\%s" % str(
                                               "hat_" + str(hat) + "_hconfid_" + str(hconfid) + "_" + str(num)+".jpg"))
            elif hat == 2 and hconfid <= 0.83:
                urllib.request.urlretrieve(img_url,
                                           "./hat/have_hat/confid_less_0.8\\%s" % str(
                                               "hat_" + str(hat) + "_hconfid_" + str(hconfid) + "_" + str(num)+".jpg"))
            elif hat == 2 and hconfid > 0.83:
                urllib.request.urlretrieve(img_url,
                                           "./hat/have_hat/confid_more_0.8\\%s" % str(
                                               "hat_" + str(hat) + "_hconfid_" + str(hconfid) + "_" + str(num)+".jpg"))


    def getage(self):
        db = connsql("192.168.11.128", 3306, "root", 'introcks1234', "intellif_face")
        sql = "SELECT (age & 15) AS age1, f.image_data,f.json,(age & 65280) / 256 AS age_ FROM intellif_face.t_face_24 f  ORDER BY TIME DESC;"
        cursor = db.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        num = 0
        for i in data:
            num += 1
            age = i[0]
            img_url = i[1]
            try:
                geconfid = json.loads(i[2])["Confidence"]['Gender']
            except:
                continue
            glconfid = json.loads(i[2])["Confidence"]['Glass']
            hconfid = json.loads(i[2])["Confidence"]['Hat']
            rconfid = json.loads(i[2])["Confidence"]['Race']
            age_ = str(i[3]).split(".")[0]

            print("年龄样本采集...第" + str(num) + "张", age, img_url, geconfid, glconfid, hconfid, rconfid, age_)
            if age == 0:
                urllib.request.urlretrieve(img_url,
                                           "./age/0\\%s" % str(
                                               "aged_" + str(age) + "_age_" + str(age_) +  "_" + str(num) + ".jpg"))
            elif age == 1:
                urllib.request.urlretrieve(img_url,
                                           "./age/1\\%s" % str(
                                               "aged_" + str(age) + "_age_" + str(age_) + "_" + str(num) + ".jpg"))
            elif age == 2:
                urllib.request.urlretrieve(img_url,
                                           "./age/2\\%s" % str(
                                               "aged_" + str(age) + "_age_" + str(age_) + "_" + str(num) + ".jpg"))
            elif age == 3:
                urllib.request.urlretrieve(img_url,
                                           "./age/3\\%s" % str(
                                               "aged_" + str(age) + "_age_" + str(age_) + "_" + str(num) + ".jpg"))
            elif age == 4:
                urllib.request.urlretrieve(img_url,
                                           "./age/4\\%s" % str(
                                               "aged_" + str(age) + "_age_" + str(age_) + "_" + str(num) + ".jpg"))
            elif age == 5:
                urllib.request.urlretrieve(img_url,
                                           "./age/5\\%s" % str(
                                               "aged_" + str(age) + "_age_" + str(age_) + "_" + str(num) + ".jpg"))
            elif age == 6:
                urllib.request.urlretrieve(img_url,
                                           "./age/6\\%s" % str(
                                               "aged_" + str(age) + "_age_" + str(age_) + "_" + str(num) + ".jpg"))
            elif age == 7:
                urllib.request.urlretrieve(img_url,
                                           "./age/7\\%s" % str(
                                               "aged_" + str(age) + "_age_" + str(age_) + "_" + str(num) + ".jpg"))
            elif age == 8:
                urllib.request.urlretrieve(img_url,
                                           "./age/8\\%s" % str(
                                               "aged_" + str(age) + "_age_" + str(age_) + "_" + str(num) + ".jpg"))
            elif age == 9:
                urllib.request.urlretrieve(img_url,
                                           "./age/9\\%s" % str(
                                               "aged_" + str(age) + "_age_" + str(age_) + "_" + str(num) + ".jpg"))

if "__name__" == "__main__":
    GetImg = GetImg("192.168.11.128", 3306, "root", 'introcks1234', "intellif_face")
    createDir()
    getGender()
    getage()
    getglasses()
    getrace()
    gethat()

