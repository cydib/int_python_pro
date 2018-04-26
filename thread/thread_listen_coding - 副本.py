#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-17 20:04:07
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import threading,time


def listen(name,now):
	print("listening:%s %s" %(name,now))
	time.sleep(2)
	print("listening 执行结束 %s"%time.strftime("%Y-%m-%d %H:%M:%S"))

def coding(name,now):
	print("coding:%s %s"%(name,now))
	time.sleep(5)
	print("coding 执行结束 %s"%time.strftime("%Y-%m-%d %H:%M:%S"))


print("单线程调用：")
listen("如果没有如果",time.strftime("%Y-%m-%d %H:%M:%S"))
coding("python", time.strftime("%Y-%m-%d %H:%M:%S"))


thread = []

t1 = threading.Thread(target=listen, args=("说散就散",time.strftime("%Y-%m-%d %H:%M:%S")))
t2 = threading.Thread(target=coding, args=("codename",time.strftime("%Y-%m-%d %H:%M:%S")))


thread.append(t1)
thread.append(t2)
# print(thread)
print("\n多线程调用：")
# t1.start()
# t2.start()
for i in thread:
	i.setDaemon(True)
	i.start()
i.join() 
