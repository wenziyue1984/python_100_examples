# -*- coding:utf-8 -*-
__author__ = 'wenziyue'

'''
将一个列表的数据复制到另一个列表中。
'''

a = [[{"a": 1234567}, 2, 3], 22222, 33333]
b = a
print(b)
print('a id:{}'.format(id(a)))
print('b id:{}'.format(id(b)))
print('a[0] id:{}'.format(id(a[0])))
print('b[0] id:{}'.format(id(b[0])))
print('a[0][0] id:{}'.format(id(a[0][0])))
print('b[0][0] id:{}'.format(id(b[0][0])))
print(a is b)
# b.append(4)
# print(a)
# a = [2, 3, 4]
# print(b)

print('*'*30)
import copy
d = copy.copy(a)
print('a id:{}'.format(id(a)))
print('d id:{}'.format(id(d)))
print('a[0] id:{}'.format(id(a[0])))
print('d[0] id:{}'.format(id(d[0])))
print('a[0][0] id:{}'.format(id(a[0][0])))
print('d[0][0] id:{}'.format(id(d[0][0])))
print(a is d)
print(a[0] is d[0])
# a.append(4)
# print(a)
# print(d)


print('*'*30)
c = copy.deepcopy(a)
print('a id:{}'.format(id(a)))
print('c id:{}'.format(id(c)))
print('a[0] id:{}'.format(id(a[0])))
print('c[0] id:{}'.format(id(c[0])))
print('a[0]["a"] id:{}'.format(id(a[0][0])))
print('c[0]["a"] id:{}'.format(id(c[0][0])))
# print(a)
# a.append(5)
# print(c)


print('*'*30)
e = a.copy()
print('a id:{}'.format(id(a)))
print('e id:{}'.format(id(e)))
print('a[0] id:{}'.format(id(a[0])))
print('e[0] id:{}'.format(id(e[0])))
print('a[0][0] id:{}'.format(id(a[0][0])))
print('e[0][0] id:{}'.format(id(e[0][0])))

'''
这篇是说复制一个list的，想到copy模块，然后顺带复习了一下深拷贝和浅拷贝以及直接赋值的不同
'''