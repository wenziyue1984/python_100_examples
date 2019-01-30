# -*- coding:utf-8 -*-
__author__ = 'wenziyue'

'''
暂停一秒输出，并格式化当前时间。 
'''

import time

if __name__=='__main__':
	t1 = time.time()
	# print(t1)
	print(time.strftime('%Y-%m-%d,%H:%M:%S', time.localtime(t1)))
	time.sleep(1)
	t2 = time.time()
	print(time.strftime('%Y-%m-%d,%H:%M:%S', time.localtime(t2)))
	print(t2-t1)

	'''时间戳'''
	print(time.time())
	'''元祖格式的时间，加不加time.time()都可以'''
	print(time.localtime())
	print(time.localtime(time.time()))
	'''格式化时间，将元祖格式的时间转成适合人看的形式（自己定义）'''
	print(time.strftime('%Y-%m-%d, %H:%M:%S', time.localtime()))
	t3 = time.strftime('%y-%m-%d,%H:%M:%S', time.localtime())
	print(t3)
	'''将格式化的时间反转成元祖格式的时间'''
	print(time.strptime(t3, '%y-%m-%d,%H:%M:%S'))

'''
学习了一下time模块
https://www.cnblogs.com/jfl-xx/p/8024596.html

https://www.cnblogs.com/sunshineyang/p/6818834.html
'''
