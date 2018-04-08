#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-13 15:25:05
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import unittest,time
from Test_interface_py_cm import Test_interface_py_cm
from HTMLTestRunner import HTMLTestRunner

test_dir = './'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')



if __name__ == "__main__":
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './report/' + now + '_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='Guest Manage System Interface Test Report',
                            description='Implementation Example with:')
    runner.run(discover)
    fp.close()


