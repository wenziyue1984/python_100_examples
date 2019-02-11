# -*- coding:utf-8 -*-
__author__ = 'wenziyue'

'''
一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
'''

def judge(num):
	if num>99999 or num<10000:
		print('不是五位数')
	else:
		a = num//10000
		b = num//1000%10
		d = num//10%10
		e = num%10
		if a == e and b == d:
			print('yes')
		else:
			print('no')


if __name__ == '__main__':
	num = input('请输入一个五位数：')
	judge(int(num))