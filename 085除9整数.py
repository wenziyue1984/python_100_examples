# -*- coding:utf-8 -*-
__author__ = 'wenziyue'

'''
输入一个奇数，然后判断最少几个 9 除于该数的结果为整数。
'''

def test(n):
	if not n % 2 == 1:
		exit('传入参数有误，请输入奇数')
	else:
		s = '9'
		index = 1
		while True:
			s_num = int(s*index)
			if s_num >= n and s_num % n == 0:
				print(s_num)
				return s_num
			index += 1


if __name__ == '__main__':
	test(13)