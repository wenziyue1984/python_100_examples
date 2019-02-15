# -*- coding:utf-8 -*-
__author__ = 'wenziyue'

'''
学习使用auto定义变量的用法。
'''

num = 2
def autofunc():
    num = 1
    print('internal block num = %d' % num)
    num += 1

for i in range(3):
    print('The num = %d' % num)
    num += 1
    autofunc()


'''
python中没有auto关键字，不太理解这是在干嘛，就直接把答案抄了上来
'''