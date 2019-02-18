# -*- coding:utf-8 -*-
__author__ = 'wenziyue'

'''
两个变量值互换
'''

def exchange(a, b):
	a, b = b, a
	return a, b


if __name__ == '__main__':
	a = 1
	b = 2
	c, d = exchange(a, b)
	print(c, d)


'''
exchange函数return a,b 返回的实际是一个tuple，（a,b）
我们可以使用两个变量来接收返回值 c, d = exchange(a, b)
也可以 c = exchange(a, b)
c = (2, 1)
'''