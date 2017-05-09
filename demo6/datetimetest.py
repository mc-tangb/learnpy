#!/usr/bin/env python
#coding:utf-8
'''
Created on 2017年5月8日
@author: 唐斌
'''

from datetime import datetime

now = datetime.now()
print(now)

print(type(now))

dt = datetime(2015, 4, 19, 12, 20)
print(dt)
#日期转timestamp
ts = dt.timestamp()
print(ts)

#timestamp 转日期
print(datetime.fromtimestamp(ts))

#str转日期
cday = datetime.strptime('2017-5-9 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)

#datetime 转换为 str

now = datetime.now()
print(now.strftime('%Y-%m-%d %H:%M:%S'))

