#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-24 21:04:21
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$
import threading
import time


class ThreadTest():

	def __init__(self):
	  pass

	def getA(self, args1, args2):
	   print("getA开始时间%s" % time.strftime("%Y-%m-%d %H:%M:%S"))
	   print("call getA",args1,args2)
	   time.sleep(1)
	   print("getA结束时间%s\n"%time.strftime("%Y-%m-%d %H:%M:%S"))
		
	def getB(self, args1, args2):
	  print("getB开始时间%s"%time.strftime("%Y-%m-%d %H:%M:%S"))
	  print("call getB",args1,args2)
	  time.sleep(2)
	  print("getB结束时间%s\n"%time.strftime("%Y-%m-%d %H:%M:%S"))

	def getC(self, args1, args2):
	  print("getC开始时间%s"%time.strftime("%Y-%m-%d %H:%M:%S"))
	  print("call getC",args1,args2)
	  time.sleep(3)
	  print("getC结束时间%s\n"%time.strftime("%Y-%m-%d %H:%M:%S"))

	def getD(self, args1, args2):
	  print("getD开始时间%s"%time.strftime("%Y-%m-%d %H:%M:%S"))
	  print("call getD",args1,args2)
	  time.sleep(10)
	  print("getD结束时间%s\n"%time.strftime("%Y-%m-%d %H:%M:%S"))

	def getE(self, args2):
	  print("getE开始时间%s"%time.strftime("%Y-%m-%d %H:%M:%S"))
	  print("call getE",args1,args2)
	  time.sleep(9)
	  print("getE结束时间%s\n"%time.strftime("%Y-%m-%d %H:%M:%S"))


if __name__ == "__main__":
	Test = ThreadTest()
	args2list = ['table1']  
	args1 = 4
	thread_ = []
	for args2 in args2list:
		t1 = threading.Thread(target=Test.getA, args = (args1, args2))
		t2 = threading.Thread(target=Test.getB, args = (args1, args2))		
		t3 = threading.Thread(target=Test.getC, args = (args1, args2))
		t4 = threading.Thread(target=Test.getD, args = (args1, args2))
		t5 = threading.Thread(target=Test.getE, args = (args2,))

		thread_.append(t1)
		thread_.append(t2)
		thread_.append(t3)
		thread_.append(t4)
		thread_.append(t5)
	# print(thread_)

	for t in thread_:
		t.setDaemon(True)
		t.start()
	for t in thread_:
		t.join()
	print("所有线程运行完毕")