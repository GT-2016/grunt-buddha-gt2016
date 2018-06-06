# coding:utf-8

# 《Python 核心编程（第二版）》书中例子演示
class WrapMe(object):
    '''授权 包装'''
    def __init__(self, obj):
        self.__data = obj

    def get(self):
        return self.__data

    def __repr__(self):
        return 'self.__data'

    def __str__(self):
        return str(self.__data)
    def __getattr__(self, item):
        return getattr(self.__data, item)

class CapOpen():
    '''包装文件对象'''
    def __init__(self, fn, mode='r', buf=-1):
        self.file = open(fn, mode, buf)

    def __str__(self):
        return str(self.file)

    def __repr__(self):
        return 'self.file'

    def write(self, line):
        self.file.write(line.upper())

    def read(self):                 # 直接用实例对象去读会报错 ‘CapOpen’ object is not iterable
        for eachLine in self.file:
            print(eachLine)

    def __iter__(self):             # 加上这个也可以不报错
        return self.file.__iter__()

    def __getattr__(self, item):
        return getattr(self.file, item)


if __name__ == '__main__':
    wrapComplex = WrapMe(3.5+4.2j)
    # print(wrapComplex)
    # print(wrapComplex.real)
    # print(wrapComplex.imag)
    # print(wrapComplex.conjugate())
    # print(wrapComplex.get())
    # ===== vars() ======== #
    # wrapComplex.foo = 100
    # wrapComplex.bar = 'Python'
    # print(wrapComplex.__dict__)
    # print(vars(wrapComplex))
    # ===== vars() ======== #
    # ======= CapOpen() =======#
    # f = CapOpen('1.txt','a')
    # f.write('hello !! welcome to python\n')
    # f.close()
    # f = CapOpen('1.txt', 'r')
    # for eachLine in f:
    #     print(eachLine)
    # f.close()
    # ====== CapOpen() =======#