# -*- coding:utf-8 -*-
from datetime import datetime

__author__ = 'wenziyue'

'''
输入某年某月某日，判断这一天是这一年的第几天？
'''

def my_fun(yy, mm, dd):
	# 判断闰年
	if (yy % 4 == 0 and yy % 100 != 0) or (yy % 400) == 0:
		feb = 29
	else:
		feb = 28
	if mm == 1:
		print(dd)
	if mm == 2:
		print(31 + dd)
	if mm == 3:
		print(dd + 31 + feb)
	if mm == 4:
		print(dd + 31 + feb + 31)
	if mm == 5:
		print(dd + 31 + feb + 31 + 30)
	if mm == 6:
		print(dd + 31 + feb + 31 + 30 + 31)
	if mm == 7:
		print(dd + 31 + feb + 31 + 30 + 31 + 30)
	if mm == 8:
		print(dd + 31 + feb + 31 + 30 + 31 + 30 + 31)
	if mm == 9:
		print(dd + 31 + feb + 31 + 30 + 31 + 30 + 31 + 31)
	if mm == 10:
		print(dd + 31 + feb + 31 + 30 + 31 + 30 + 31 + 31 + 30)
	if mm == 11:
		print(dd + 31 + feb + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31)
	if mm == 12:
		print(dd + 31 + feb + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30)
	
def other_fun(yy, mm, dd):
	months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
	if (yy % 4 == 0 and yy % 100 != 0) or (yy % 400 == 0):
		sum = months[mm-1] + dd + 1
	else:
		sum = months[mm-1] + dd
	print(sum)

if __name__=="__main__":
	try:
		date_str = input('请输入日期(yyyy-mm-dd)：')
		datetime.strptime(date_str, '%Y-%m-%d')
		date_split = date_str.split('-')
		yy = int(date_split[0])
		mm = int(date_split[1])
		dd = int(date_split[2])
		my_fun(yy, mm, dd)
		other_fun(yy, mm, dd)
	except ValueError as e:
		# print(e)
		print('日期输入格式有误')

'''
两种方法思路相同，但是写法上有很大不同，都是累加前面的月份，但是我的方法要一遍一遍的判断月份，看起来很冗长，
而他们的利用list下标，直接从list中取出要累加的值，看起来简洁许多许多
通过datetime.strptime()转时间单位来校验输入的日期格式是否正确
tips：遇到这种要写很多if判断的情况可以考虑利用下标在list中取值
'''