# -*- coding:utf-8 -*-
__author__ = 'wenziyue'

'''
查找字符串。
查找某字符串中
'''

import re

if __name__ == '__main__':
	s1 = 'wenziyue1984 want to be better'
	s2 = '1984'
	s3 = '1983'
	print(s1.find(s2))
	print(s1.find(s3))

	s_re = re.findall('(.*?)want to be better', s1)
	print(s_re)

'''
字符串操作
s1.find(s2) 返回s1中s2的下标，如不存在返回-1
re模块 一般用的方法re.findall()是匹配字符串中的正则
re.findall('(.*?) want to be better', s1)
'''