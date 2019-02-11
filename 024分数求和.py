# -*- coding:utf-8 -*-
__author__ = 'wenziyue'

'''
有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
'''

def get_fbnq(num):
	if num == 1:
		return 1
	if num == 2:
		return 2
	return get_fbnq(num-1) + get_fbnq(num-2)

def get_num(num):
	return get_fbnq(num+1)/get_fbnq(num)

def get_add(num):
	num_list = []
	for i in range(1, num+1):
		num_list.append(get_num(i))
	return sum(num_list)

'''答案方法（比我写的方法更好）'''
def get_result():
	a = 1
	b = 2
	s = 0
	for i in range(1, 21):
		s += b/a
		# n = b
		# b += a
		# a = n
		a, b = b, a+b # 两种写法都可以
	print(s)

if __name__ == '__main__':
	print(get_add(20))
	get_result()