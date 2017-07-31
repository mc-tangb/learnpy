#!/usr/bin/env python
#coding:utf-8
'''
Created on 2017年5月9日
@author: 唐斌
'''

import base64

a = base64.b64encode(b'abcd')

print(a)

b = base64.b64decode(a)

def safe_encode(bstr):
    
    s = base64.b64encode(bstr)
    while s.endswith(b'='):
        s = s[0:-1]
    return s

def safe_decode(bstr):
    while len(bstr) % 4 < 4 and len(bstr) % 4 > 0:
        bstr += b'='
        
    return base64.b64decode(bstr)
     
    
m = safe_encode(b'abcd')
print(m)

n = safe_decode(m)
print(n)