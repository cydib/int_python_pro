# -*- coding: utf-8 -*-
import MySQLdb, urllib.request,os


def get_Pic(sql):
	db = MySQLdb.connect("192.168.11.128", "root", "introcks1234", "intellif_face")
	cursor = db.cursor()
	cursor.execute(sql)
	data = cursor.fetchall()
	num = 0
	for i in data:
		num += 1
		for j in i:
			#image_data字段无ip时
			# j = "http://192.168.11.65" + j
			# 128环境是7，65环境是9
			name = j.split("/")[7].split(".")[0]
			print("正在下载第 %d 张 %s"%(num,name+".jpg"))
			urllib.request.urlretrieve(j, "F:\\temp\\pic\\%s.jpg" %str(name))



get_Pic("select f.image_data from intellif_face.t_face_24 f where  ((f.gender & 112) / 16) <= 5  order by time desc;")
get_Pic("select  f.image_data from intellif_face.t_face_24 f where  ((f.race & 112) / 16) <= 5 and f.source_id=4 order by time desc;")
get_Pic("select  f.image_data from intellif_face.t_face_24 f where  ((f.accessories & 112) / 16) <= 5 and f.source_id=10 order by time desc;")
get_Pic("select  f.image_data from intellif_face.t_face_24 f where  ((f.age & 112) / 16) <= 5 and f.source_id=10 order by time desc;")
get_Pic("select  f.image_data from intellif_face.t_face_24 f where  ((f.accessories & 28672) / 4096) <= 5 and f.source_id=10 order by time desc;")