# -*- coding:utf-8 -*-
__author__ = 'wenziyue'

'''
字符串日期转换为易读的日期格式。
'''

from dateutil import parser

if __name__ == '__main__':
	dt = parser.parse("Aug 28 2015 12:00AM")
	print(dt)


'''
str转换为date格式：
from datetime import datetime
d = datetime.strptime('2000-01-01', '%Y-%m-%d) # 字符串转datetime格式
d_s = d.strftime('%Y年 %m月 %d日') # datetime转指定格式的str

总结：
str转datetime：datetime.strptime(str, '%Y%m%d')
datetime转str：d.strftime('%Y%m%d')
'''