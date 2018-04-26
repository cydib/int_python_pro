#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-24 17:42:15
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
age_ = 0
ageimgpath = []
ageduan = []	
for k in range(0, 10):
    ageimgpath.append("./age/" + str(k))
    ageduan.append(k)
agelist = dict(zip(ageduan, ageimgpath))
# print(agelist)
for k, j in agelist.items():
            if age_ == k:
                print(j,k)
else:
	print(123)