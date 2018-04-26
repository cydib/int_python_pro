#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-13 09:45:14
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os,xlrd,xlwt,random,linecache,re
from xlwt import *      
from xlwt import *      

testdata = {"cofid":0.7934,'gender':1}

def statis(file):
	with open(file, 'r',encoding='UTF-8') as f:
		num = 0
		for i in f.readlines():		
			confid = i.split(",")[0].split("：")[1]
			gender = i.split(",")[1].split("：")[1]
			img = i.split(",")[2].split("：")[1].strip()
			# print(img,gender,confid)
			# print(num,float(confid[:3]),float(confid[:3])>0.5)
			if (float(confid[:3]) >= 0.5 and int(gender)==2):
				num +=1
		print("识别正确 %d 个,识别错误：%s 个" %(num,(10000-int(num))))
for file in os.listdir("./"):
	result = re.compile("*.txt")
	# statis('./f2_result_py.txt')






# with open('./f2_result_py.txt', 'r',encoding='UTF-8') as f:
# 	flist = []
# 	for i in f.readlines():
# 		img = i.split(",")[2].split("：")[1].strip()
# 		# if ".png" in img:
# 		# 	img1=img.replace(".png","")
# 		confid = i.split(",")[0].split("：")[1]
# 		gender = i.split(",")[1].split("：")[1]


# 		flist.append(img)
# 		flist.append(gender)
# 		flist.append(confid)

		
# 	print(sorted(flist))

		