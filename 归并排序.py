#!/usr/bin/env python
# !coding:utf-8

# 归并排序（英语：Merge sort，或mergesort），是创建在归并操作上的一种有效的排序算法。该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。
#分治法:
#    分割：递归地把当前序列平均分割成两半。
#    集成：在保持元素顺序的同时将上一步得到的子序列集成到一起（归并）。

import random

def SortByMerge(arr,size):
    if size <= 1:
        return arr

    i = int(size/2)
    left = SortByMerge(arr[:i], i)
    right = SortByMerge(arr[i:], size - i)
    return MergeSort(left, right)


def MergeSort(left, right):
    # 比较传过来的两个序列left,right，返回一个排好的序列
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]  # 这时候i或者j到了序列的最后
    result += right[j:]
    return result

list1=random.sample(range(20),20)  #生成无序list
print('waiting sort list:',list1[:])
print('sort ok list:',SortByMerge(list1,len(list1)))


