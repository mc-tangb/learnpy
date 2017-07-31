#!/usr/bin/env python
#coding:utf-8
'''
Created on 2017年5月6日
@author: 唐斌
'''

from functools import reduce
import functools

def fn(x, y):
    return x * 10 + y

def test1():
    '''
    map 函数：接收两个参数，第一个参数是函数， 第二个参数是Iterable,map将传入的函数依次作用到序列的每个元素上
    '''
    li = list(map(str, [1, 2, 3, 5, 6]))
    print(li)
    
    '''reduce, 把一个函数作用在一个序列上，这个函数接收两个参数,reduce把结果继续和序列的下一个元素做累计运算'''   
    
    re = reduce(fn, [1, 3, 5, 7, 9])
    print(re)

'''实现list列表内的字符串首字母大写'''   
def test2(li):
    
    if isinstance(li, list) == False:
        print('必须传入list类型')
        return
    
    return list(map(str.capitalize, li))

'''实现list内数字相乘'''       
def prod(li):
    if isinstance(li, list) == False:
        print('必须传入list类型')
        return
    return reduce(lambda x,y: x*y, li)
    
'''实现字符串转换float'''    
def strtof(string): 
    table = {'0': 0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7': 7, '8':8, '9':9}
    index = string.index('.')
    s1 = string[0:index]
    s2 = string[:index:-1]
    
    r1 = reduce(lambda x,y: x*10 + y, map(lambda x: table[x], s1))
    r2 = reduce(lambda x,y: (x/10 + y), map(lambda x: table[x], s2))/10
    
    return r1+r2

print(strtof('1123.31231'))


'''filter'''
def test3():
    def odd(x):
        if x%2 == 0:
            return True
        else:
            return False
    
    print(list(filter(odd, [1,2,3,4,5])))


'''sorted'''
def test4():
    L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
    print(sorted(L, key=lambda t: t[0].lower()))
    


'''装饰器'''

'''不带参数的装饰器'''    
def log(func):
    @functools.wraps(func)
    def wraper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wraper

'''带参数的装饰器'''
def log1(text):
    def decorator(func):
        @functools.wraps(func)
        def wraper(*args, **kw):
            print('%s %s():' %(text, func.__name__))
            return func(*args, **kw)
        return wraper
    return decorator

@log
def fn_test():
    print("hahaha")

@log1('sabi')
def fn_test1():
    print("hahaha1")
    
if __name__ == '__main__':
    test1()
    print(test2(['qiaoming', 'liumin', 'chenduci']))
    print(prod([1, 2, 3, 4, 5, 6]))
    test3()
    test4()
    
    fn_test()
    fn_test1()