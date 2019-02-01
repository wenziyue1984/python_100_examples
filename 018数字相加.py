# -*- coding:utf-8 -*-
__author__ = 'wenziyue'

'''
求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
'''

def add_num(num, index):
	num_list = []
	for i in range(1, index+1):
		num_list.append(num*i)
	result = 0
	for i in [int(x) for x in num_list]:
		result += i
	print(result)


if __name__ == '__main__':
	num = input('请输入数字：')
	index = input('请输入相加次数：')
	add_num(num, int(index))

'''
我需要一些东西鼓励我，但是不希望是朋友圈，显得傻乎乎的，想在soul发，但也不希望再有羁绊
'''