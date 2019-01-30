# -*- coding:utf-8 -*-
__author__ = 'wenziyue'

'''
有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
'''

test_list = []
for i in range(1,5):
	for j in range(1, 5):
		for k in range(1, 5):
			if(i!=j and i!=k and j!=k):
				test_list.append(i*100+j*10+k)

for i in test_list: print(i)
print("共能组成{}个三位数".format(len(test_list)))