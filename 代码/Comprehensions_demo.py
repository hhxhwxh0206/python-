#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
功能：学习生成式使用
作者：ithh <hhxhwxh@qq.com>
时间：Fri Sep 18 15:05:13 2020
"""

# 列表生成式
# list()方法 + 迭代器
l1 = list(range(10))
print(l1)
l2 = [x for x in range(10)]
l2 = [x ** 2 for x in range(10)]
l2 = [x ** 2 for x in range(10) if x % 3 == 0]
'''
l2 =[]
for x in range(10):
    if x % 3 == 0:
        a = x ** 2
        l2.append(a)
'''
l2 = [m + n for m in 'ABC' for n in 'XYZ']
print(l2)
# 集合生成式类似列表只是使用'{}'



# --------------------------------------------------


# 字典生成式
# d = {key: value for (key, value) in iterable} 
data1 = {'x': 1, 'y': 2, 'z': 3}
b = ['java','python','perl']  
s = [89,90,91] 
data2 = {k + '1': v ** 2 for k, v in data1.items()}
data2 = {k + '1': v ** 2 for k, v in zip(b, s)}
print(zip(b,s))
<zip object at 0x000002C70E3A2F00>
{'java1': 7921, 'python1': 8100, 'perl1': 8281}
print(data1.items())
dict_items([('x', 1), ('y', 2), ('z', 3)])
print(data2)

# --------------------------------------------------  '-'.center(50,'-')

d = {}  
for i,n in zip(b,s):  
    if n >= 90:  
        d[i] = n  
print(d) #{'python': 90, 'perl': 91}  
d = {i:n for i,n in zip(b,s) if n >=90 }  
print(d) #{'python': 90, 'perl': 91}  

# --------------------------------------------------

d = {}  
#双重for in 循环  
for i in range(1,4):  
    for n in range(1,4):  
        d[i] = n  
print(d) #{1: 3, 2: 3, 3: 3} 因为key唯一，后面的key:value都被1:3 2:3 3:3覆盖掉了  
  
# 字典生成式  
d = {i:n for i in range(1,4) for n in range(1,4)}  
print(d) # {1: 3, 2: 3, 3: 3}  

# --------------------------------------------------

d = {}  
# 双重for in循环，嵌套if  
for i in range(1,4):  
    for n in range(1,4):  
        if n < 3:  
           d.update([(i,n)])  
print(d) #{1: 2, 2: 2, 3: 2}  
  
# 字典生成式  
d = {i:n for i in range(1,4) for n in range(1,4) if n <3}  
print(d) #{1: 2, 2: 2, 3: 2}  

a = '-'.center()