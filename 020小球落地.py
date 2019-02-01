# -*- coding:utf-8 -*-
__author__ = 'wenziyue'

'''
一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
'''

def fall(num):
	s = 100
	high = 100
	index = 1
	while index < num:
		high /= 2
		s += high*2
		index += 1
	print('第{}次落地时小球经过了{}米，下一次会反弹{}米高'.format(num, s, high/2))

if __name__ == '__main__':
	fall(10)