# -*- coding:utf-8 -*-
__author__ = 'wenziyue'

'''
从键盘输入一些字符，逐个把它们写到磁盘文件上，直到输入一个 # 为止。
'''

import codecs



def test():
	with codecs.open('097_test.txt', 'w') as file:
		while True:
			s = input('请输入字符：')
			if s == '#':
				break
			else:
				file.write(s)


if __name__ == '__main__':
	test()