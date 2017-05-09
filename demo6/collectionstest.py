#!/usr/bin/env python
#coding:utf-8
'''
Created on 2017年5月9日
@author: 唐斌
'''

from collections import namedtuple
from collections import deque

#坐标定义
Point = namedtuple('Point', ['x', 'y'])

p = Point(1, 2)
print(p.x)
print(p.y)

#高效插入和删除的列表

q = deque(['a', 'b'])

q.append('x')
q.appendleft('y')

print(q)
q.pop()
print(q)
q.popleft()

print(q)

#defaultdict key不存在时返回默认值
from collections import defaultdict
dd = defaultdict(lambda: None)
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])

#OrderedDict 保持key的顺序

from collections import OrderedDict

d = dict([('a',1), ('c', 2), ('b', 3)])

print(d)

d1= OrderedDict([('a',1), ('c', 2), ('b', 3)])
print(d1)

#Counter 简单计数器

from collections import Counter
c = Counter()

for ch in 'programming':
    c[ch] = c[ch] + 1
    
print(c)



