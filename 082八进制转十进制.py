# -*- coding:utf-8 -*-
__author__ = 'wenziyue'

'''
八进制转换为十进制
'''

if __name__ == '__main__':
    n = 0
    p = input('input a octal number:')
    for i in range(len(p)):
        n = n * 8 + ord(p[i]) - ord('0')
    print(n)


'''
不会，没仔细看，感觉很少会用到
'''