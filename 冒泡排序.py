#!/usr/bin/env python
# !coding:utf-8

#冒泡排序（Bubble Sort）
# 它重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。
# 走访数列的工作是重复地进行直到没有再需要交换。
import random

def paosort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if (arr[j] > arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr



list1=random.sample(range(20),20)  #生成无序list
print('waiting sort list:',list1[:])
print('sort ok list:',paosort(list1))
