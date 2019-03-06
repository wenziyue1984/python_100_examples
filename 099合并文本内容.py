# -*- coding:utf-8 -*-
__author__ = 'wenziyue'

'''
有两个磁盘文件A和B,各存放一行字母,要求把这两个文件中的信息合并(按字母顺序排列), 输出到一个新文件C中。 
'''

import codecs

def test():
	a = ''
	with codecs.open('099a.txt', 'r') as file:
		a = file.read()
	b = ''
	with codecs.open('099b.txt', 'r') as file:
		b = file.read()
	c = sorted([a, b])
	s = ''.join(c)
	with codecs.open('099c.txt', 'w') as file:
		file.write(s)


if __name__ == '__main__':
	test()