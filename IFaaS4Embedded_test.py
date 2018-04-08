#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-19 16:37:59
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import ctypes
from ctypes import *


ll = ctypes.cdll.LoadLibrary   
lib = ll("./libIFaaS4EAlgSDK.so") 
 
lib.IFaaS4E_Alg_Init()


 
