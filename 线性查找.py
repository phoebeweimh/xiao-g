#!/usr/bin/env python
# !coding:utf-8
#线性查找指按一定的顺序检查数组中每一个元素，直到找到所要寻找的特定值为止。
import random
#待查找列表
checklist=[]
for i in range(1,31):
    checklist.append(i)
print('待查找列表',checklist)

#待查找元素
x = random.choice(checklist)
print('待查找元素',x)

#线性查找
def line_check(c_list, val):
    i=0
    for j in range(len(c_list)-1):
        if val==c_list[j]:
            i=1
            return j
    if i==0:
        return print('待查元素不在待查列表中')
ret = line_check(checklist, x)
print('待查找元素在列表中的位置是：',ret)

