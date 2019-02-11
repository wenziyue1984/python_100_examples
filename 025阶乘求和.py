# -*- coding:utf-8 -*-
__author__ = 'wenziyue'

'''
求1+2!+3!+...+20!的和。
'''

def get_num(num):
	s = 1
	for i in range(1, num+1):
		s *= i
	return s

def get_result(num):
	num_list = []
	for i in range(1, num+1):
		num_list.append(get_num(i))
	return sum(num_list)

'''答案方法（比我的好，主要是找到了每一项之间的关系）'''
def get_result2():
	n = 1
	s = 0
	for i in range(1, 21):
		n *= i
		s += n
	print(s)


if __name__ == '__main__':
	print(get_result(20))
	get_result2()