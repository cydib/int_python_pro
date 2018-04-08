#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-20 15:31:53
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import _thread
import time


# 为线程定义一个函数
def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s: %s" % (time.ctime(time.time()),threadName))


# 创建两个线程
try:
    _thread.start_new_thread(print_time, ("Thread-1", 0,))
    _thread.start_new_thread(print_time, ("Thread-2", 0,))
except:
    print("Error: unable to start thread")

while 1:
    pass