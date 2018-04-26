# -*- coding: utf-8 -*-
import MySQLdb
import urllib.request
import os


def get_Pic(sql):
    db = MySQLdb.connect("192.168.11.128", "root",
                         "introcks1234", "intellif_face")
    cursor = db.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    num = 0
    os.system("mkdir pic1")
    for i in data:
        num += 1
        for j in i:
            # image_data字段无ip时
            # j = "http://192.168.11.65" + j
            # 128环境是7，65环境是9
            name = j.split("/")[7].split(".")[0]
            print("正在下载第 %d 张 %s" % (num, name + ".jpg"))
            urllib.request.urlretrieve(j, ".\\pic1\\%s.jpg" % str(name))


get_Pic(
    "SELECT  f.image_data FROM intellif_face.t_face_24 f where((gender & 112) / 16) <= 5 ORDER BY TIME DESC limit 10")
# get_Pic(
#     "SELECT  f.image_data FROM intellif_face.t_face_24 f where((race & 112) / 16) <= 5 ORDER BY TIME DESC")
# get_Pic(
#     "SELECT  f.image_data FROM intellif_face.t_face_24 f where((accessories & 112) / 16) <= 5 ORDER BY TIME DESC")
# get_Pic(
#     "SELECT  f.image_data FROM intellif_face.t_face_24 f where((age & 112) / 16) <= 5 ORDER BY TIME DESC ")
# get_Pic(
#     "SELECT  f.image_data FROM intellif_face.t_face_24 f where((accessories & 28672) / 4096) <= 5 ORDER BY TIME DESC")
