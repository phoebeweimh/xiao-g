#!/usr/bin/env python
# !coding:utf-8

#30 个人在一条船上，超载，需要 15 人下船。报数，从 1 开始，数到 9 的人下船。

#给人编号
peple =[]
for i in range(1,31):
    person = 'person%d'%i
    peple.append(person)

c = 0 #9的循环
max =30  #人数最大值

#遍历人数
while max >15:
    god = []
    for pe in peple:
        c += 1
        if c % 9 == 0:
            print(c,pe,'离开')
            max -= 1
            god.append(pe)
    for pe in god:
        peple.remove(pe)
print('留下人员',peple)