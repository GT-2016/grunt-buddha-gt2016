# coding:utf-8
'''
@ 描述符举例
'''
import os
from os.path import getsize
# 获取文件大小
# print(getsize('1.txt'))

class DevNull(object):
    def __get__(self, instance, owner):
        pass
    def __set__(self, instance, value):
        pass

class DevNull2(object):
    def __get__(self, instance, owner):
        print('ignoring...')
    def __set__(self, instance, value):
        print('%r...ignoring'%value)
class DevNull3(object):

    def __init__(self, name=None):
        self.name = name

    def __get__(self, instance, owner):
        print('ignoring...[%s]'%self.name)
    def __set__(self, instance, value):
        print('set %r. to [%s]..ignoring'%(value,self.name))

class C1(object):
    foo = DevNull()

class C2(object):
    foo = DevNull2()

class C3(object):
    ''' 验证__call__ '''
    def __call__(self, *args, **kwargs):    # 'C3' object is not callable
        pass
    foo = DevNull3('foo')
# c1 = C1()
# c1.foo = 'bar'
# print(c1.foo)           # None
#
# c2 = C2()
# c2.foo = 'bar'
# print(c2.foo)           # None

# c3 = C3()
# c3.foo = 'bar'
# print(c3.foo)           # None

ret = os.fork()         # 只在linux中有这个命令
if ret == 0:
    print('child')
else:
    print('parent')