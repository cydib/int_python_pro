#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-12 17:27:26
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os

def getGender(path):
	cout = 0
	for img in os.listdir(path):
		cout += 1
		# print(img,cout)
		gender = img.split("__")[1].split("_")[1]
		confid1 = img.split("__")[1].split("_")[3]
		if ".jpg" in confid1:
			confid = confid1.replace('.jpg','')
		oriimg = img.split("__")[0]
		print("置信度：%s , 性别：%s , 图像：%s.png "%(confid,gender,oriimg))

if __name__ == '__main__':
	getGender("")
# getGender('./f_img_result')
