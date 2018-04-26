#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-26 11:14:20
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$
# 运行前先请先安装python3第三方库:pip install mysqlclient

import os, MySQLdb, urllib.request, json, time, threading


class GetImg():

    def __init__(self, ip, port, username, password, database):
        self.db = MySQLdb.connect(host=ip, port=port, user=username, passwd=password, db=database, charset="utf8")
        self.cursor = self.db.cursor()
        self.gefcl = "./gender/female/confid_less_0.8"
        self.gefcm = "./gender/female/confid_more_0.8"
        self.gemcm = "./gender/male/confid_more_0.8"
        self.gemcl = "./gender/male/confid_less_0.8"
        self.geucl = "./gender/unknow/confid_less_0.8"
        self.geucm = "./gender/unknow/confid_more_0.8"

        self.rahcl = "./race/han/confid_less_0.8"
        self.rahcm = "./race/han/confid_more_0.8"
        self.raocm = "./race/other/confid_more_0.8"
        self.raocl = "./race/other/confid_less_0.8"

        self.glucl = "./glasses/unknow/confid_less_0.8"
        self.glucm = "./glasses/unknow/confid_more_0.8"
        self.glncl = "./glasses/No_glasses/confid_less_0.8"
        self.glncm = "./glasses/No_glasses/confid_more_0.8"
        self.glocl = "./glasses/Ordinary_glasses/confid_less_0.8"
        self.glocm = "./glasses/Ordinary_glasses/confid_more_0.8"
        self.glscl = "./glasses/sunglasses/confid_less_0.8"
        self.glscm = "./glasses/sunglasses/confid_more_0.8"

        self.hahcl = "./hat/have_hat/confid_less_0.8"
        self.hahcm = "./hat/have_hat/confid_more_0.8"
        self.hancm = "./hat/no_hat/confid_more_0.8"
        self.hancl = "./hat/no_hat/confid_less_0.8"
        self.haucm = "./hat/unknow/confid_more_0.8"
        self.haucl = "./hat/unknow/confid_less_0.8"

    def createDir(self):

        os.makedirs(self.gefcl, exist_ok=True)
        os.makedirs(self.gefcm, exist_ok=True)
        os.makedirs(self.gemcm, exist_ok=True)
        os.makedirs(self.gemcl, exist_ok=True)
        os.makedirs(self.geucl, exist_ok=True)
        os.makedirs(self.geucm, exist_ok=True)

        os.makedirs(self.rahcl, exist_ok=True)
        os.makedirs(self.rahcm, exist_ok=True)
        os.makedirs(self.raocm, exist_ok=True)
        os.makedirs(self.raocl, exist_ok=True)

        os.makedirs(self.glucl, exist_ok=True)
        os.makedirs(self.glucm, exist_ok=True)
        os.makedirs(self.glncl, exist_ok=True)
        os.makedirs(self.glncm, exist_ok=True)
        os.makedirs(self.glocl, exist_ok=True)
        os.makedirs(self.glocm, exist_ok=True)
        os.makedirs(self.glscl, exist_ok=True)
        os.makedirs(self.glscm, exist_ok=True)

        os.makedirs(self.hahcl, exist_ok=True)
        os.makedirs(self.hahcm, exist_ok=True)
        os.makedirs(self.hancm, exist_ok=True)
        os.makedirs(self.hancl, exist_ok=True)
        os.makedirs(self.haucm, exist_ok=True)
        os.makedirs(self.haucl, exist_ok=True)

        for i in range(0, 10):
            os.makedirs("./age/%s" % i, exist_ok=True)

    def getAll(self, confid_, tablename):
        sql = "SELECT (gender & 15) AS gender1,(race & 15) AS race1,(accessories & 15) AS glasses1,(accessories & 3840) / 256 AS hat1,(age & 65280) / 256 AS age,(age & 15) AS age1 ,f.image_data,f.json FROM  intellif_face." + tablename + " f WHERE f.json like '%Confidence%';"
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        num = 0

        ageimgpath = []
        ageduan = []
        for k in range(0, 10):
            ageimgpath.append("./age/" + str(k))
            ageduan.append(k)
        agelist = dict(zip(ageduan, ageimgpath))


        for i in data:
            num += 1
            gender_ = i[0]
            race_ = i[1]
            glasses_ = i[2]
            hat_ = str(i[3]).split(".")[0]
            age_ = str(i[4]).split(".")[0]
            age_group = i[5]
            img_url = i[6]
            try:
                geconfid = json.loads(i[7])["Confidence"]['Gender']
                glconfid = json.loads(i[7])["Confidence"]['Glass']
                hconfid = json.loads(i[7])["Confidence"]['Hat']
                rconfid = json.loads(i[7])["Confidence"]['Race']
            except:
                continue

            print("第 " + str(num) + " 条", gender_, glasses_, hat_, race_, age_group,age_,  img_url, geconfid, glconfid,
                  hconfid, rconfid)
            '''
            性别
            
            '''

            if gender_ == 2 and geconfid <= confid_:
                urllib.request.urlretrieve(img_url,
                                           self.gefcl + "\\%s" % str(
                                               "gender_" + str(gender_) + "_gconfid_" + str(geconfid) + "_" + str(
                                                   num) + ".jpg"))
            elif gender_ == 2 and geconfid > confid_:
                urllib.request.urlretrieve(img_url,
                                           self.gefcm + "\\%s" % str(
                                               "gender_" + str(gender_) + "_gconfid_" + str(geconfid) + "_" + str(
                                                   num) + ".jpg"))
            elif gender_ == 1 and geconfid <= confid_:
                urllib.request.urlretrieve(img_url,
                                           self.gemcl + "\\%s" % str(
                                               "gender_" + str(gender_) + "_gconfid_" + str(geconfid) + "_" + str(
                                                   num) + ".jpg"))
            elif gender_ == 1 and geconfid > confid_:
                urllib.request.urlretrieve(img_url,
                                           self.gemcm + "\\%s" % str(
                                               "gender_" + str(gender_) + "_gconfid_" + str(geconfid) + "_" + str(
                                                   num) + ".jpg"))
            elif gender_ == 0 and geconfid <= confid_:
                urllib.request.urlretrieve(img_url,
                                           self.geucl + "\\%s" % str(
                                               "gender_" + str(gender_) + "_gconfid_" + str(geconfid) + "_" + str(
                                                   num) + ".jpg"))
            elif gender_ == 0 and geconfid > confid_:
                urllib.request.urlretrieve(img_url,
                                           self.geucm + "\\%s" % str(
                                               "gender_" + str(gender_) + "_gconfid_" + str(geconfid) + "_" + str(
                                                   num) + ".jpg"))


            '''
            眼镜
            '''
            if glasses_ == 0 and glconfid <= confid_:
                urllib.request.urlretrieve(img_url,
                                           self.glucl + "\\%s" % str(
                                               "glasses_" + str(glasses_) + "_glconfid_" + str(glconfid) + "_" + str(
                                                   num) + ".jpg"))
            elif glasses_ == 0 and glconfid > confid_:
                urllib.request.urlretrieve(img_url,
                                           self.glucm + "\\%s" % str(
                                               "glasses_" + str(glasses_) + "_glconfid_" + str(glconfid) + "_" + str(
                                                   num) + ".jpg"))
            elif glasses_ == 1 and glconfid <= confid_:
                urllib.request.urlretrieve(img_url,
                                           self.glncl + "\\%s" % str(
                                               "glasses_" + str(glasses_) + "_glconfid_" + str(glconfid) + "_" + str(
                                                   num) + ".jpg"))
            elif glasses_ == 1 and glconfid > confid_:
                urllib.request.urlretrieve(img_url,
                                           self.glncm + "\\%s" % str(
                                               "glasses_" + str(glasses_) + "_glconfid_" + str(glconfid) + "_" + str(
                                                   num) + ".jpg"))
            elif glasses_ == 2 and glconfid <= confid_:
                urllib.request.urlretrieve(img_url,
                                           self.glocl + "\\%s" % str(
                                               "glasses_" + str(glasses_) + "_glconfid_" + str(glconfid) + "_" + str(
                                                   num) + ".jpg"))
            elif glasses_ == 2 and glconfid > confid_:
                urllib.request.urlretrieve(img_url,
                                           self.glocm + "\\%s" % str(
                                               "glasses_" + str(glasses_) + "_glconfid_" + str(glconfid) + "_" + str(
                                                   num) + ".jpg"))
            elif glasses_ == 3 and glconfid <= confid_:
                urllib.request.urlretrieve(img_url,
                                           self.glscl + "\\%s" % str(
                                               "glasses_" + str(glasses_) + "_glconfid_" + str(glconfid) + "_" + str(
                                                   num) + ".jpg"))
            elif glasses_ == 3 and glconfid > confid_:
                urllib.request.urlretrieve(img_url,
                                           self.glscm + "\\%s" % str(
                                               "glasses_" + str(glasses_) + "_glconfid_" + str(glconfid) + "_" + str(
                                                   num) + ".jpg"))


            '''
            帽子
            '''

            if int(hat_) == 0 and hconfid <= confid_:
                urllib.request.urlretrieve(img_url,
                                           self.haucl + "\\%s" % str(
                                               "hat_" + str(hat_) + "_hconfid_" + str(hconfid) + "_" + str(
                                                   num) + ".jpg"))
            elif int(hat_) == 0 and hconfid > confid_:
                urllib.request.urlretrieve(img_url,
                                           self.haucm + "\\%s" % str(
                                               "hat_" + str(hat_) + "_hconfid_" + str(hconfid) + "_" + str(
                                                   num) + ".jpg"))
            elif int(hat_) == 1 and hconfid <= confid_:
                urllib.request.urlretrieve(img_url,
                                           self.hancl + "\\%s" % str(
                                               "hat_" + str(hat_) + "_hconfid_" + str(hconfid) + "_" + str(
                                                   num) + ".jpg"))
            elif int(hat_) == 1 and hconfid > confid_:
                urllib.request.urlretrieve(img_url,
                                           self.hancm + "\\%s" % str(
                                               "hat_" + str(hat_) + "_hconfid_" + str(hconfid) + "_" + str(
                                                   num) + ".jpg"))
            elif int(hat_) == 2 and hconfid <= confid_:
                urllib.request.urlretrieve(img_url,
                                           self.hahcl + "\\%s" % str(
                                               "hat_" + str(hat_) + "_hconfid_" + str(hconfid) + "_" + str(
                                                   num) + ".jpg"))
            elif int(hat_) == 2 and hconfid > confid_:
                urllib.request.urlretrieve(img_url,
                                           self.hahcm + "\\%s" % str(
                                               "hat_" + str(hat_) + "_hconfid_" + str(hconfid) + "_" + str(
                                                   num) + ".jpg"))


            '''
            种族
            '''

            if race_ == 0 and rconfid <= confid_:
                urllib.request.urlretrieve(img_url,
                                           self.rahcl + "\\%s" % str(
                                               "race_" + str(race_) + "_rconfid_" + str(rconfid) + "_" + str(
                                                   num) + ".jpg"))
            elif race_ == 0 and rconfid > confid_:
                urllib.request.urlretrieve(img_url,
                                           self.rahcm + "\\%s" % str(
                                               "race_" + str(race_) + "_rconfid_" + str(rconfid) + "_" + str(
                                                   num) + ".jpg"))
            elif race_ == 1 and rconfid <= confid_:
                urllib.request.urlretrieve(img_url,
                                           self.raocl + "\\%s" % str(
                                               "race_" + str(race_) + "_rconfid_" + str(rconfid) + "_" + str(
                                                   num) + ".jpg"))
            elif race_ == 1 and rconfid > confid_:
                urllib.request.urlretrieve(img_url,
                                           self.raocm + "\\%s" % str(
                                               "race_" + str(race_) + "_rconfid_" + str(rconfid) + "_" + str(
                                                   num) + ".jpg"))


            '''
            年龄
            '''

            for k, j in agelist.items():
                if age_group == k:
                    urllib.request.urlretrieve(img_url,
                                               j + "\\%s" % str(
                                                   "agegroup_" + str(age_group) + "_age_" + str(age_) + "_" + str(num) + ".jpg"))

    def count(self):
        gelist = [self.gefcl, self.gefcm, self.gemcm, self.gemcl, self.geucl, self.geucm]
        gesum = 0
        for ge in gelist:
            gesum += int(len(os.listdir(ge)))
        now = time.strftime("%Y-%m-%d %H:%M:%S")
        print("\n%s 采集结束:\n" % now)
        print(" 性别样本共采集：%s 张 " % gesum)

        ralist = [self.rahcl, self.rahcm, self.raocm, self.raocl]
        rasum = 0
        for ra in ralist:
            rasum += int(len(os.listdir(ra)))
        print(" 种族样本共采集：%s 张 " % rasum)

        gllist = [self.glucl, self.glucm, self.glncl, self.glncm, self.glocl, self.glocm, self.glscl, self.glscm]
        glsum = 0
        for i in gllist:
            glsum += int(len(os.listdir(i)))
        print(" 眼镜样本共采集：%s 张 " % glsum)

        halist = [self.hahcl, self.hahcm, self.hancm, self.hancl, self.haucm, self.haucl]
        hasum = 0
        for i in halist:
            hasum += int(len(os.listdir(i)))
        print(" 帽子样本共采集：%s 张 " % hasum)

        agelist = []
        for j in range(0, 10):
            agelist.append("./age/" + str(j))

        agsum = 0
        for ag in agelist:
            agsum += int(len(os.listdir(ag)))
        print(" 年龄样本共采集：%s 张 " % agsum)


if __name__ == "__main__":
    GetImg = GetImg("192.168.11.128", 3306, "root", 'introcks1234', "intellif_face")
    tablelist = ['t_face_24']  # 可以增加表名
    confid = 0.83
    GetImg.createDir()
    for tablename in tablelist:
        GetImg.getAll(confid,tablename)
    GetImg.count()