#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-09 17:52:01
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import re

key = "<html><body><h1>hello world<h1></body></html>"#这段是你要匹配的文本
p1 = "(?<=<h1>).+?(?=<h1>)"#这是我们写的正则表达式规则，你现在可以不理解啥意思
pattern1 = re.compile(p1)#我们在编译这段正则表达式
matcher1 = re.search(pattern1,key)#在源文本中搜索符合正则表达式的部分
print (matcher1.group(0))#打印出来

key = "javapythonhtmlvhdl"#这是源文本
p1 = "python"#这是我们写的正则表达式
pattern1 = re.compile(p1)#同样是编译
matcher1 = re.search(pattern1,key)#同样是查询
print (matcher1.group(0))


key = r"<h1>hello world<h1>"#源文本
p1 = r"<h1>.+<h1>"#我们写的正则表达式，下面会将为什么
pattern1 = re.compile(p1)
print(pattern1.findall(key))#发没发现，我怎么写成findall了？咋变了呢？