#!/usr/bin/env python
#coding:utf-8
'''
Created on 2017年7月31日
@author: 唐斌
'''

arr = ['suzhou', 'hangzhou', 'yangzhou']

arr[0] = 'hanzhong'

print(arr)

arr.append('xi\'an')
print(arr)

arr.insert(1, 'wuhan')
print(arr)

del arr[0] #删除元素
print(arr)

arr.pop(1)
print(arr)

arr.remove('wuhan')
print(arr)

# list 排序
arr.append('guangzhou')
print(arr)
arr.sort()
print(arr)
arr.sort(reverse=True)

print(sorted(arr, reverse=True))
print(arr)
print(len(arr))









