#!/usr/bin/env python
# !coding:utf-8

import random
# 定义函数
def lcm(x, y):
    #  获取最大的数
    if x > y:
        greater = x
    else:
        greater = y

    while (True):
        if ((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1

    return lcm

num1 = random.randint(1,1000)
num2 = random.randint(1, 1000)
print( num1,"和", num2,"的最小公倍数为", lcm(num1, num2))
