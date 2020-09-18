#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
功能：练习装饰器，生成器，迭代器
作者：ithh
时间：Fri Aug 28 11:32:50 2020
"""

import time

def time_use(fn):
    # 计算函数用时
    start = time.time()
    fn()
    end = time.time()
    return "用时" , start - end



def funA(fn) :
    print ('A')
    fn()
    # 执行传入的 fn 参数
    return  'fkit' 
'''
下面的装饰效果相当于 funA(funB)
funB 将会被替换（装饰）成该语句的返回值
由于 funA 函数返回 fkit ，因此 funB 就是 fkit
'''
@time_use
def funB () :
    print ('B')
# print(funB) # fkit
 

''' 
    global_fn = lambda p: print('执行 lambda 表达式，p 参数：',p)
    class Category:
        cate_fn = lambda p: print ('执行 lambda 表达式，p 参数：',p)
    # 调用全局空间内的 global_fn ，为参数 p 传入参数值
    global_fn ('fkit')
    c = Category()
    # 调用类命名空间内的 cate fn, Python 自动绑定第一个参数
    c.cate_fn()
'''


# 创建生成器

'''
1 定义一个包含 yield 语句的函数。
2 调用第1步创建的函数得到生成器

使用for表达式创建使用"()"
'''

def test(val, step) :
    print("----函数开始执行---- ")
    cur = 0
    # 遍历 0～val
    for i in range(val) :
        # cur 添加 i*step
        cur += i * step   
        yield cur


'''
yield cur 语句的作用 有两点。
1 每次返回一个值，有点类似于 return 语句 。
2 冻结执行，程序每次执行到 yield 语句时就会被暂停 。
在程序被 y ield 语句冻结之后，当程序再次调用next()函数获取生成器的下一个值时 ，
程序才会继续向下执行 。需要指出的是调用包含yield语句的函数并不会立即执行，
它只是返回一个生成器只有当程序通过next() 函数调用生成器或遍历生成器时，函数才会真正执行
'''
# t = test(10, 2)
# print('================')
# print(next(t))
# print(next(t))