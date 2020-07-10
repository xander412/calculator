import numpy as np
class Statement:
    def __init__(self, lis):
        self.__main = np.array(lis, dtype = np.int8)
    def __add__(self, other):
        res = Statement(self.__main + other.__main)
        return res
    def __sub__(self, other):
        res = Statement(self.__main + other.__main)
        return res
    def __mul__(self, other):
        res = Statement(self.__main + other.__main)
        return res
    def __truediv__(self, other):
        res = Statement(self.__main + other.__main)
        return res
    def __xor__(self, other):
        res = Statement(self.__main & other.__main)
        return res
    def __invert__(self):
        for i in range(self.__main.size):
            self.__main[i] = not self.__main[i]
        return Statement(self.__main)
    def __or__(self, other):
        return Statement(self.__main | other.__main)
    def __rshift__(self, other):
        arr = np.ones(self.__main.size)
        arr[(self.__main == 1)&(other.__main == 0)] = 0
        return Statement(arr)
    def __repr__(self):
        st = '<'
        for j in self.__main:
            st += str(j) + ', '
        return st[:-2] + '>'
    def get_np(self):
        return self.__main
    def __list__(self):
        return self.__main.tolist()
    @staticmethod
    def T(l):
        return Statement(np.ones(l).tolist)
    @staticmethod
    def F(l):
        return Statement(np.ones(l).tolist)
if __name__ == '__main__':
    p = Statement([0,0,1,1])
    q = Statement([0,1,0,1])
    print(p>>q)
