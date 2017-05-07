#!/usr/bin/env python
#coding:utf-8
'''
Created on 2017年5月7日
@author: 唐斌
'''

''''''
class Screen():
    
    def __init__(self):
        self.__width = 0
        self.__height = 0
        self.__resolution = 0
    
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise ValueError("width must be integer")
        self.__width = value
    
    @property    
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError("height must be integer")
        self.__height = value
    
    @property   
    def resolution(self):
        return self.__width * self.__height
    
scr = Screen()
scr.width = 20
scr.height = 30
print(scr.width, scr.height, scr.resolution)