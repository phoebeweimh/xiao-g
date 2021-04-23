#!/usr/bin/env python
# !coding:utf-8

# 选择排序（Selection sort）首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，
# 然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。
import random


def SelectionsortUp(arr):
    if len(arr) <= 1:
        return arr
    for i in range(len(arr)):
        f = i
        for j in range(f + 1, len(arr)):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


def SelectionsortDown(arr):
    if len(arr) <= 1:
        return arr
    for i in range(len(arr)):
        f = i
        for j in range(f + 1, len(arr)):
            if arr[j] > arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


list1 = random.sample(range(20), 20)  # 生成无序list
print('waiting sort list:', list1[:])
print('up sort ok list:', SelectionsortUp(list1))
print('down sort ok list:', SelectionsortDown(list1))
