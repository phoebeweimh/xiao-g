#!/usr/bin/env python
# !coding:utf-8

zhishu = []
f = 0
for num in range(0,1000):
    if num > 1:
        # 查看因子
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            zhishu.append(num)
           # f =+ 1
#print('总共有',f,'个质数')
print(zhishu[:])

