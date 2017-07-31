#!/usr/bin/env python
# --*-- encoding=utf-8 --*--

'''使用方法修改字符串的大小写'''
name = "ada lovepython"
print(name.title()) # str.title() 字符串首字母大写的操作

print(name.upper()) # str.upper()字符串全部大写的方法

print(name.lower()) 

# 字符串拼接 
strand = name + ' knhd'

print(strand)

name1 = '  andk ak '
print(name1 + 'abc') 
print(name1.rstrip() + 'abc')
print(name1.lstrip() + 'abc')
print(name1.strip() + 'abc')


