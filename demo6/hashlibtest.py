#!/usr/bin/env python
#coding:utf-8
'''
Created on 2017年5月10日
@author: 唐斌
'''

import hashlib

md5 = hashlib.md5()

md5.update('how to use md5 in python hashlib'.encode('utf-8'))
print(md5.hexdigest())
