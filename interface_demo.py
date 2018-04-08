#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-08 18:26:38
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$


import unittest,requests,json;

class Test_interface_py_cm(unittest.TestCase):

	def setUp(self):
		# print("<<<<<< start test >>>>>>")
		self.base_url = "http://192.168.11.67:8063/api/"
		self.s = requests.Session()
		self.headers = {'content-type': 'application/json;charset=UTF-8'}

	def tearDown(self):
		print("<<<<<< end test >>>>>>")


	def test1(self):
		data ={"minTimes": 9}
		r = self.s.post(self.base_url + "intellif/mining/analysis/community/stranger/list/page/1/pagesize/100",data=json.dumps(data),headers=self.headers)
		r.connection.close()
		print(r.json())


def runner():
	suite = unittest.TestSuite()
	suite.addTest(Test_interface_py_cm('test1'))
	unittest.TextTestRunner().run(suite)

if __name__ == '__main__':
	runner()
	