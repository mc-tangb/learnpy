#!/usr/bin/env python
#coding:utf-8
'''
Created on 2017年5月10日
@author: 唐斌
'''

import struct

# 将任意数据类型转换成bytes
# 
byt = struct.pack('>I', 123456)
print(byt)
