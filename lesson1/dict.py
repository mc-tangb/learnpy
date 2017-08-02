#!/usr/bin/env python
#coding:utf-8
'''
Created on 2017年8月2日
@author: 唐斌
'''

alien_0 = {
    'color': 'green',
    'points': 5
}

print(alien_0['color'])

del alien_0['color']
print(alien_0)

user_0 = {
    'username': 'tangbin',
    'first': 'tang',
    'last': 'bin'
}

print(user_0.items())
for key, value in user_0.items():
    print(key + ":" + value)

print(user_0.keys())
for key in user_0.keys():
    print(key)
    
favourite_language = {
    'lisa': 'Python',
    'lili': 'Java',
    'chars': 'C',
    'Danny': 'Python'
}

languages = favourite_language.values()
print(languages)
print(set(languages))