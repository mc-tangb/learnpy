#!/usr/bin/env python
#coding:utf-8
'''
Created on 2017年5月7日
@author: 唐斌
'''

def demo1():
    f = open('../demo4/oop.py', 'r', encoding="utf-8")
    print(f.read())
    f.close()
    
    with open('./test.txt', 'w') as f:
        f.write('hello world')
    
if __name__ == '__main__' :
    demo1()