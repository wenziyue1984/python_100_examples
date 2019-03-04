# -*- coding:utf-8 -*-
__author__ = 'wenziyue'

'''
时间函数举例3
'''

import time

if __name__ == '__main__':
    start = time.clock()
    for i in range(10000):
        print(i)
    end = time.clock()
    print('different is %6.3f' % (end - start))


'''
time.clock()在python3.3之后已被弃用
time.clock() 函数以浮点数计算的秒数返回当前的CPU时间。用来衡量不同程序的耗时，比time.time()更有用。
在第一次调用的时候，返回的是程序运行的实际时间；
以第二次之后的调用，返回的是自第一次调用后,到这次调用的时间间隔
'''