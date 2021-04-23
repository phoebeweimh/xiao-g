#!/usr/bin/env python
# !coding:utf-8
import random

def hcf(x, y):
    """该函数返回两个数的最大公约数"""

    # 获取最小值
    if x > y:
        smaller = y
    else:
        smaller = x

    for i in range(1, smaller + 1):
        if ((x % i == 0) and (y % i == 0)):
            hcf = i

    return hcf


num1 = random.randint(1,1000)
num2 = random.randint(1, 1000)

print(num1, "和", num2, "的最大公约数为", hcf(num1, num2))