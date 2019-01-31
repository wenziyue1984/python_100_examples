# -*- coding:utf-8 -*-
__author__ = 'wenziyue'

'''
输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
'''

def tongji(str):
	alpha = 0
	digit = 0
	space = 0
	for i in str:
		if i.isalpha():
			alpha += 1
		if i.isdigit():
			digit += 1
		if i.isspace():
			space += 1
	print('字符总数：{}，字母：{}，数字：{}，空格：{}，其他字符：{}'
		  .format(len(str), alpha, digit, space, len(str)-alpha-digit-space))

if __name__=='__main__':
	tongji('abc *** 1234 $%^/')

'''
学习了怎么统计字符，python太方便了，有专门的函数，不用自己再搞
isdigit， isdigit， isspace
'''