# -*- coding:utf-8 -*-
__author__ = 'wenziyue'

'''
从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个磁盘文件"test"中保存。 
'''

import codecs

def test():
	s = input('请输入一串字母：')
	s_new = s.upper()
	with codecs.open('098_test.txt', 'w') as file:
		file.write(s_new)


if __name__ == '__main__':
	test()