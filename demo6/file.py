#!/usr/bin/env python
#coding:utf-8
'''
Created on 2017年5月8日
@author: 唐斌
'''
import os
with open('./file.txt', 'w') as f:
    f.write('hello world')

print(help(os))
