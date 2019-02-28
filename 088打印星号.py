# -*- coding:utf-8 -*-
__author__ = 'wenziyue'


'''
读取7个数（1—50）的整数值，每读取一个值，程序打印出该值个数的＊。
'''

def test():
	index = 0
	while index < 7:
		num = input('请输入整数：')
		if num.isdigit() and 1 <= int(num) <= 50:
			print('*' * int(num))
			index += 1
		else:
			print('输入有误，请重新输入')


if __name__ == '__main__':
	test()