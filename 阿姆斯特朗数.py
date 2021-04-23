#!/usr/bin/env python
# !coding:utf-8

#阿姆斯特朗数：一个n位正整数等于其各位数字的n次方之和
alist=[]
for i in range(1,1001):
    temp = i
    sum = 0
    l = len(str(temp))
    while temp > 0:
        shu = temp % 10
        sum += shu ** l
        temp //= 10
    if sum==i:
        alist.append(i)
print('1000以内阿姆斯特朗数:',alist)
