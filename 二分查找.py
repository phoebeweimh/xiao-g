#!/usr/bin/env python
# !coding:utf-8

#二分搜索是一种在有序数组中查找某一特定元素的搜索算法。
# 搜索过程从数组的中间元素开始，如果中间元素正好是要查找的元素，则搜索过程结束；
# 如果某一特定元素大于或者小于中间元素，则在数组大于或小于中间元素的那一半中查找，而且跟开始一样从中间元素开始比较。
# 如果在某一步骤数组为空，则代表找不到。这种搜索算法每一次比较都使搜索范围缩小一半。

import random
#待查找列表
checklist=[]
for i in range(1,31):
    checklist.append(i)
print('待查找列表',checklist)

#待查找元素
x = random.choice(checklist)
print('待查找元素',x)

#二分查找
def erfencheck(c_list, val):
    low = 0                         # 最小数下标
    high = len(c_list) - 1       # 最大数下标
    while low <= high:
        mid = (low + high) // 2     # 中间数下标
        if c_list[mid] == val:   # 如果中间数下标等于val, 返回
            return mid
        elif c_list[mid] > val:  # 如果val在中间数左边, 移动high下标
            high = mid - 1
        else:                       # 如果val在中间数右边, 移动low下标
            low = mid + 1
    return # val不存在, 返回None

ret = erfencheck(checklist, x)
print('待查找元素在列表中的位置是：',ret)
