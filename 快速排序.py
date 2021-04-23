#!/usr/bin/env python
# !coding:utf-8

# 快速排序使用分治法（Divide and conquer）策略来把一个序列（list）分为较小和较大的2个子序列，然后递归地排序两个子序列。
#步骤为：挑选基准值：从数列中挑出一个元素，称为"基准"（pivot）;
#    分割：重新排序数列，所有比基准值小的元素摆放在基准前面，所有比基准值大的元素摆在基准后面（与基准值相等的数可以到任何一边）。在这个分割结束之后，对基准值的排序就已经完成;
#    递归排序子序列：递归地将小于基准值元素的子序列和大于基准值元素的子序列排序。
#递归到最底部的判断条件是数列的大小是零或一，此时该数列显然已经有序。
#选取基准值有数种具体方法，此选取方法对排序的时间性能有决定性影响。
import random
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

list1=random.sample(range(20),20)  #生成无序list
print('waiting sort list:',list1[:])
print('sort ok list:',quicksort(list1))