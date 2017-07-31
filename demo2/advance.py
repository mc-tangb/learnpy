#!/usr/bin/env python
#coding:utf-8
'''
Created on 2017年5月5日
@author: 唐斌
'''
from collections import Iterable
import os

def demo1():
    '''切片'''
    a = [1, 'as', 2, 'd', 4, 'fg']
    print(a[2:4])
    print(a[-1::-1])
    print(a)
    
    '''迭代'''
    ''''判断对象是否可迭代'''
    flag = isinstance(a, Iterable)
    print(flag)
    for i in a:
        print(i)
        
    '''实现下标索引迭代'''
    for i,v in enumerate(a):
        print(i, v)
    
    for x,y in [[1,2], [3,4], (4,6)]:
        print(x,y)
        
        
    '''列表生成式'''
    li = list(range(0,11))
    print(li)
    
    aa = [x*y for x in range(0,10) for y in range(10, 20)]
    print(aa)
    
    d = [d for d in os.listdir('.')]
    print(d)
    
    '''生成器'''
    g = (x*x for x in range(10))
    print(g)
    print(g.next())
    
'''杨辉三角''' 
def triggle():
    a = [1]
    while True:
        yield a
        a = [v+a[i+1] for i,v in enumerate(a) if i<len(a)-1]
        a.insert(0,1)
        a.append(1)
        
        
n = 0;    
for i in triggle():
    n += 1
    print(i)
    if n > 10:
        break




if __name__ == '__main__':
    '''demo1()'''