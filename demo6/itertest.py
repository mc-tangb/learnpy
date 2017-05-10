#!/usr/bin/env python
#coding:utf-8
'''
Created on 2017年5月10日
@author: 唐斌
'''

import itertools

#创建停不下来的序列
'''
natuals = itertools.count()
for n in natuals:
    print(n)
   
cs = itertools.cycle('ABC')
for c in cs:
    print(c)

'''

#将一个元素重复下去
'''
ns = itertools.repeat('A', 10)
for n in ns:
    print(n)
'''    
# 利用takewhile 截取一段

natuals = itertools.count()
ns = itertools.takewhile(lambda x: x<20, natuals)
print(list(ns))

#拼接迭代串
for c in itertools.chain('ABC', 'XYZ'):
    print(c)
    
# groupby

for key, value in itertools.groupby('AABCABCDDSSDCA'):
    print(key, list(value))