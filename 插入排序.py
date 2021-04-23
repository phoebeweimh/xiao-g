#!/usr/bin/env python
# !coding:utf-8

#
import random
#生成无序list
list1=random.sample(range(20),20)
print('待排序列表:',list1[:])

for i in range(1,len(list1)):
	for j in reversed(range(i)): #列表角标倒序
		if list1[j+1]<list1[j]:
			list1[j],list1[j+1]=list1[j+1],list1[j]
print('排序后列表:',list1[:])
