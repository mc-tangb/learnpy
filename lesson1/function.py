#!/usr/bin/env python
#coding:utf-8
'''
Created on 2017年8月2日
@author: 唐斌
'''

def test(*args):
    for val in args:
        print(val)
    
test('a', 1, 2, 'ba', 'c22')

def test1(**args):
    for key, val in args.items():
        print(key + ":" + val);
    
test1(name='abc', age='26', c3='25,45,68', fro='sx')