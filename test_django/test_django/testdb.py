#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-04 20:25:38
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from django.http import HttpResponse

from TestModel.models import Test

def testdb(request):
	test1 = Test(name='runoob')
	test2 = Test(name2='test_name')
	test1.save()
	test2.save()
	return HttpResponse("<p>数据添加成功！</p>")