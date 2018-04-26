#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-12 21:13:54
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os,xlrd


with open('./f_results.txt', 'r') as f:
	print(f.read().split("\\")[1])