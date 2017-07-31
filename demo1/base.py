#!/usr/bin/env python
#coding:utf-8
'''
Created on 2017年5月4日
@author: 唐斌
'''

def test1 (): 
    n = 123
    f = 456.789
    s1 = 'Hello, world'
    s2 = 'hello, \\\'Adam\\\''
    s3 = r'Hello, "Bart"'
    s4 = r'''Hello,
    Lisa'''
    
    print(n)
    print(f)
    print(s1)
    print(s2)
    print(s3)
    print(s4)
    
test1()

def test2():
    '''
        ord() 获取字符的证书编码表示， chr() 将编码转换成对应的字符
    '''
    a = ord('A')
    b = chr(25991)
    print(a)
    print(b)
    
test2()

def test3():
    '''
    str.encode() 方法可以将字符串编码为指定的bytes
    '''
    a = '中文'.encode('utf-8')
    print(a)
    
    '''
            将bytes变为str, 就需要使用encode() 方法
    '''
    
    b = b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
    print(b)
    
    '''
            要计算str包含多少个字符 可以使用  len(),
    计算字符数,如果转换成bytes就会计算字节数
    '''
    
    size1 = len('百家姓')
    print(size1)
    
    size2 = len('百家姓'.encode('utf-8'))
    print(size2)
    
test3()

def test4():
    '''
    字符串格式化
    常见占位符： 
    %d  ----  整数
    %f  ----  浮点数
    %s  ----  字符串
    %x  ----  十六进制数
    '''
    s = 'hello, %s' % 'world'
    print(s)
    
    s2 = 'Hi, %s, you have $%d' % ('Micheal', 100000)
    print(s2)
    
    s3 = '%2d-%02d' % (3, 1)
    print(s3)
    
    s4 = '%6.2f' % 3.1415926
    print(s4)
    
    '''
    如果不确定用什么, %s 就是一个不错的选择
    '''
    
    s5 = 'Age: %s, Gender: %s' % (25, True)
    print(s5)
    
    '''
    如果需要用到%, 那就需要去转义, 使用这样 %%。
    '''
    
    s6 = 'growth rate :%d%%' % 7
    print(s6)
    
    c1 = 72
    c2 = 85
    r = 100*(c2-c1)/c1
    print('%3.1f' % r)
test4()

'''
list and tuple
'''
def test5():
    mates = ['Micheal', 'Bob', 'Tracy']
    print(mates)
    
    print(len(mates))
    
    '''取最后一个元素,依次类推'''
    print(mates[-1])
    
    '''向数组添加元素'''
    mates.append('Adam') 
    print(mates)
    
    '''将元素插到数组的指定位置'''
    mates.insert(1, 'liming')
    print(mates)
    
    '''删除最后一个元素用pop(), '''
    mates.pop()
    print(mates)
    
    '''删除指定元素用pop(i)'''
    mates.pop(1)
    print(mates)
   
    '''元素更新'''
    mates[0] = 'xiaoxia'
    print(mates)
    
    '''也可以是一个list'''
    mates[-1] = [1, 2 ,3]
    print(mates)
    
    '''元组同list一样，只是不可修改，即没有insert, append 和赋值方法'''
    
    tpmates = ('xiaoxia', 'liming')
    print(tpmates[-1])
    print(tpmates[1])
    
'''条件判断'''
def test6():
    '''
    if 条件一:
        block1
    elif 条件2:
        block2
    elif 条件3:
        block3
    else:
        block4
    
    '''
    
    weight = 49
    if weight < 50:
        print('你太瘦了!')
    elif weight < 65:
        print('你的体重太标准了')
    elif weight < 70:
        print('注意锻炼哦！')
    else:
        print('你就是个死胖子！')

'''循环'''
def test7():
    names = ['xiaom', 'liming', 'dnas']
    for name in names:
        print(name)
        
    total = 0
    for i in range(10):
        total += i
    
    print(total) 

'''dict and set'''
def test8():
    d = {
        'micheal' : 95,
        'bob': 75,
        'Tracy': 87
        }
    print(d['micheal'])
    
    '''访问不存在的key,会报错'''
    '''print(d['aa'])'''
    
    '''判断key 是否存在'''
    print('aa' in d)
    print(d.get('aa'))
    
    '''删除key'''
    d.pop('micheal')
    print(d)
    
    s = set([1,2,3])
    print(s)
    
    s.add(4)
    print(s)
    
    s.remove(1)
    print(s)
    '''不能将可变对象放入set, 这样会无法比较两个对象是否相等'''
    '''s.add([1,2])'''
  
if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
    test8()
    
    