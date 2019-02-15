# -*- coding:utf-8 -*-
__author__ = 'wenziyue'

'''
模仿静态变量的用法。
'''

def varfunc():
    var = 0
    print('var = %d' % var)
    var += 1
if __name__ == '__main__':
    for i in range(3):
        varfunc()

# 类的属性
# 作为类的一个属性吧
class Static:
    StaticVar = 5
    def varfunc(self):
        self.StaticVar += 1
        print(self.StaticVar)

print(Static.StaticVar)
a = Static()
for i in range(3):
    a.varfunc()


'''
python是动态语言，不存在完全静态的变量，所以这里的静态变量指的就是类变量

java静态变量的介绍：
大家都知道，我们可以基于一个类创建多个该类的对象，每个对象都拥有自己的成员，互相独立。然而在某些时候，
我们更希望该类所有的对象共享同一个成员。此时就是 static 大显身手的时候了！！
Java 中被 static 修饰的成员称为静态成员或类成员。它属于整个类所有，而不是某个对象所有，即被类的所有对象所共享。
静态成员可以使用类名直接访问，也可以使用对象名进行访问。当然，鉴于他作用的特殊性更推荐用类名访问
静态变量可以被修改，凡是变量都可以被修改
'''