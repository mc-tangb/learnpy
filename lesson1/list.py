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

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ', that was a great trick!')
print(magicians[0:3])
print(magicians[:1])
print(magicians[1:])
print(magicians[-2:])    
magicians2 = magicians[:]
magicians2[0].title()
print(magicians)
print(magicians2)

    
for i in range(1, 5):
    print (i)
    
print(list(range(1, 6)))

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
    
print(squares)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))
    
squares2 = [square**2 for square in range(1, 11)]
print(squares2)

del squares2[0]
print(squares2)









