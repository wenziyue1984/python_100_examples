# -*- coding:utf-8 -*-
__author__ = 'wenziyue'

'''
编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n
'''

def test(n):
	if n % 2 == 0:
		num = 0
		for i in range(1, n+1):
			if i % 2 == 0:
				num += 1/i
		return num
	elif n % 2 == 1:
		num = 0
		for i in range(1, n+1):
			if i % 2 == 1:
				num += 1/i
		return num


if __name__ == '__main__':
	n = input('请输入一个正整数：')
	result = test(int(n))
	print(result)