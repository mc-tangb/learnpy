#!/usr/bin/env python
#coding:utf-8
'''
Created on 2017年5月5日
@author: 唐斌
'''

''' 函数  '''
def test1():
    '''返回绝对值'''
    print(abs(100))
    print(abs(-20))
    
    '''最值'''
    print(max(1,2))
    print(max(1,45,3,6))
    print(min(1,4,6,2))
    
    '''数据类型转换'''
    print(int('1213'))
    print(float('12.34'))
    print(str(1232.23))
    print(bool(2))
    print(bool(0))
    
    a = 256
    print(hex(a))
    
'''函数定义'''
def func():
    print('a')

'''调用'''
func()

def func1(x):
    if x >= 0:
        return x
    else:
        return -x
    
print(func1(2))

def noop():
    '''什么都不做'''
    pass

noop()

def func3(x,y,c=1):
    '''返回多个值'''
    return x+y, c

x,y = func3(1,2,3)
print(x,y)

'''收集参数'''
def func4(a, b, *args):
    print('a=', a, ' b=', b, ' args=', args)

func4(1,2,'a', 'ssds', 4)

def func5(a, b, **args):
    print('a=', a, ' b=', b, ' args=', args)
    
func5(1,2,c=4,d='4')

'''递归'''
def func6(n):
    if n == 1:
        print('*')
        return 1
    print('*'*n)
    return func6(n-1)
    
func6(5)    
       
if __name__ == '__main__':
    test1()