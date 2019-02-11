# -*- coding:utf-8 -*-
__author__ = 'wenziyue'

'''
给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
'''

def test(num):
	a = num//10000
	b = num//1000%10
	c = num//100%10
	d = num//10%10
	e = num%10

	# 五位数
	if a != 0:
		print(e, d, c, b, a)
		print('5位数')
		return
	# 四位数
	if b != 0:
		print(e, d, c, b)
		print('4位数')
		return
	# 三位数
	if c != 0:
		print(e, d, c)
		print('3位数')
		return
	# 二位数
	if d != 0:
		print(e, d)
		print('2位数')
		return
	# 一位数
	print(e)
	print('1位数')

	'''还可以写成下面这种形式，用elif代替return'''
	# # 五位数
	# if a != 0:
	# 	print(e, d, c, b, a)
	# 	print('5位数')
	# # 四位数
	# elif b != 0:
	# 	print(e, d, c, b)
	# 	print('4位数')
	# # 三位数
	# elif c != 0:
	# 	print(e, d, c)
	# 	print('3位数')
	# # 二位数
	# elif d != 0:
	# 	print(e, d)
	# 	print('2位数')
	# # 一位数
	# else:
	# 	print(e)
	# 	print('1位数')


if __name__ == '__main__':
	num = input('请输入一个不多于5位的正整数：')
	test(int(num))