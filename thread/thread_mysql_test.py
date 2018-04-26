#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-25 18:04:06
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import threading,time,MySQLdb

class TestMysql():

	def __init__(self, ip, port, username, password, database):
		self.db = MySQLdb.connect(host=ip, port=port, user=username, passwd=password, db=database, charset="utf8")
		self.cursor = self.db.cursor()

	def select1(self,tablename):
		sql = "SELECT (gender & 15) AS gender1, f.image_data,f.json FROM intellif_face." + tablename + " f limit 1;"
		self.cursor.execute(sql)
		data = self.cursor.fetchone()

		print(data)

	def select2(self,tablename):
		sql = "SELECT (race & 15) AS race1,f.image_data,f.json FROM intellif_face." + tablename + " f limit 1;"
		self.cursor.execute(sql)
		data = self.cursor.fetchone()

		print(data)




if __name__ == '__main__':
	test = TestMysql("192.168.11.128", 3306, "root", 'introcks1234', "intellif_face")
	tablelist = ['t_face_24','t_face_25','t_face_26']  # 可以增加表名
	thread = []
	for tablename in tablelist:
		print(tablename)
		t1 = threading.Thread(target = test.select1, args = (tablename,))
		t2 = threading.Thread(target = test.select2, args = (tablename,))
		thread.append(t1)
		thread.append(t2)
	for t in thread:
		t.start()
