#!/usr/bin/env python
# !coding:utf-8

import random

#生成华氏温度
huashi1 = random.randint(1,200)
print('华氏温度为:',huashi1)
# 华氏温度转摄氏温度
sheshi1 = (huashi1 * 1.8) + 32
print('%0.1f 华氏温度转为摄氏温度为 %0.1f ' % (huashi1, sheshi1))

#生成摄氏温度
sheshi2  = random.randint(1,100)
print('摄氏温度为:',sheshi2)
# 华氏温度转摄氏温度
huashi2 = (sheshi2 - 32) /  1.8
print('%0.1f 摄氏温度转为华氏温度为 %0.1f ' % (sheshi2, huashi2))
