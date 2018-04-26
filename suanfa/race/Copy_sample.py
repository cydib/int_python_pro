#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-20 11:02:36
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os,shutil,random
# file = "no_weizu_sample.txt"
# cou = 0
# with open(file, 'r',encoding='UTF-8') as f:
# 		for j in f.readlines():
# 			cou += 1
# 			if "\n" in j:
# 				img = j.replace('\n','')
# 			for i in os.listdir("E:\\intellif\\算法\\种族\\0419\\notweizu"):
# 				if img == i:
# 					print(i)
# 					shutil.copy(i,"E:\\intellif\\算法\\种族\\result\\not_weizu_sample\\")

 
def random_copyfile(srcPath,dstPath,numfiles):
	name_list = list(os.path.join(srcPath,name) for name in os.listdir(srcPath))
	random_name_list = list(random.sample(name_list,numfiles))
	if not os.path.exists(dstPath):
		os.mkdir(dstPath)
	for oldname in random_name_list:
		print(oldname.split("\\")[-1])
		shutil.copyfile(oldname,oldname.replace(srcPath, dstPath))

srcPath="E:\\intellif\\算法\\种族\\0419\\weizu"        
dstPath = "E:\\intellif\\算法\\种族\\samples\\weizu"
random_copyfile(srcPath,dstPath,3015)
