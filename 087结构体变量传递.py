# -*- coding:utf-8 -*-
__author__ = 'wenziyue'


'''
结构体变量传递
'''

if __name__ == '__main__':
    class Student:
        x = 0
        c = 0
    def f(stu):
        stu.x = 20
        stu.c = 'c'
    a = Student()
    a.x = 3
    a.c = 'a'
    f(a)
    print(a.x, a.c)
