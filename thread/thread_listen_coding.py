#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-17 20:04:07
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import threading,time

class Test:

	def listen(self,name,now):
		print("listening:%s %s" %(name,now))
		time.sleep(2)
		print("listen 执行结束 %s"%time.strftime("%Y-%m-%d %H:%M:%S"))

	def coding(self,name,now):
		print("coding:%s %s"%(name,now))
		time.sleep(5)
		print("coding 执行结束 %s"%time.strftime("%Y-%m-%d %H:%M:%S"))

Test = Test()
print("单线程调用：")
Test.listen("如果没有如果",time.strftime("%Y-%m-%d %H:%M:%S"))
Test.coding("python", time.strftime("%Y-%m-%d %H:%M:%S"))


thread = []
gname = "123"

t1 = threading.Thread(target=Test.listen,args=(gname,now1)
t2 = threading.Thread(target=Test.coding,args=(codename,now2)

thread.append(t1)
thread.append(t2)
print("\n多线程调用：")
# t1.start()
# t2.start()
for i in thread:
	i.setDaemon(True)
	i.start()
i.join() 
