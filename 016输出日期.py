# -*- coding:utf-8 -*-
__author__ = 'wenziyue'

'''
输出指定格式的日期
'''

from datetime import datetime

def print_date(date_str):
	try:
		date = datetime.strptime(date_str, '%Y-%m-%d')
		print(date.strftime('%Y--%m--%d'))
		print('{}年{}月{}日'.format(date.year, date.month, date.day))
	except ValueError as e:
		print(e)


if __name__=='__main__':
	# date = input('请输入日期（yyyy-mm-dd）：')
	print_date('2000-01-01')

'''
主要练习了使用datetime模块，
字符串转datetime：datetime.strptime
datetime转字符串：datetime.strftime		注意：strftime('xxx')里不能有汉字
'''