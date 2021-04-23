#!/usr/bin/env python
# !coding:utf-8

import random

red = []                #定义红色球列表
blue = []              #定义蓝色球列表
i = 1

#生成红色球数字
while i < 7:
	f1 = random.randint(1,34)
	if f1 not in red:    #判定红色球结果不是重复的结果
		red.append(f1)
		i += 1

#生成蓝色球数字
blue.append(random.randint(1,17))

#输出结果
print('红色球为：',sorted(red))  #排序输出结果
print('蓝色球为：',blue)