#!/usr/bin/env python
# !coding:utf-8

# 斐波那契数列指：第0项是0，第1项是第一个1。从第三项开始，每一项都等于前两项之和。
import random

num = random.randint(0, 20)
print('斐波拉契数列位数为：', num)


def fab(num):
    a, b = 0, 1
    fablist = []
    if num <= 0:
        print('生成的数不对')
    elif num == 1:
        fablist.append(a)
        return fablist
    else:
        fablist.append(a)
        fablist.append(b)
        for i in range(1, num - 1):
            a, b = b, a + b
            fablist.append(b)
        return fablist


print('斐波拉契数列为', fab(num))
