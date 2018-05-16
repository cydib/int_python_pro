#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-02 09:55:39
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$
def tupleParem(*t):
    print(t, type(t))


def dictParam(**d):
    print(d, type(d))


def accept1(*s):
    print(sum(s))
    print(sum(list1))


def accept2(**s):
    print(s)
    print(list2)

def mean(one,*other):
    '''
    把某函数接收到的除了第一个参数之外的所有参数输出
    '''
    print(other)

def foo(a,b,*args,**kwargs):
    print('a = ',a)
    print('b = ',b)
    print('args = ',args)
    print('kwargs = ',kwargs)

def kw_dict(*args,**kwargs):
    print(args,kwargs)
    return args,kwargs
tupleParem()
# dictParam(a=1, b=2)
# list1 = (0, 1, 2, 3, 7.5)
# list2 = {'a': 0, 'b': 1, 'c': 2}
# accept1(*list1)
# accept2(**list2)
# mean('milk','oranage','branana')
foo(1,'b',a1=1,a2=2)
kw_dict(1,a=1,b=2)