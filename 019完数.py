# -*- coding:utf-8 -*-
__author__ = 'wenziyue'

'''
一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
'''

def get_ws():
	result = {}
	for i in range(1, 1000):
		yinzi_list = []
		for index in range(1, round(i/2)+1):
			if i % index == 0:
				yinzi_list.append(index)
		if i == sum(yinzi_list):
			result[i] = yinzi_list
	return result

if __name__ == '__main__':
	print(get_ws())