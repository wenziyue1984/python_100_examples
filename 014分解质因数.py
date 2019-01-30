# -*- coding:utf-8 -*-
__author__ = 'wenziyue'

'''
将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
'''

def zhishu(num):
	for i in range(2, int(num)):
		if num % i == 0:
			return False
	return True

def get_num(num):
	num_list = []
	zs_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
	shang = num
	for i in zs_list:
		while (shang % i == 0):
			num_list.append(i)
			shang /= i
			if zhishu(shang):
				num_list.append(int(shang))
				return num_list
		continue

if __name__=='__main__':
	print(get_num(774))