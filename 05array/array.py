# -*- coding: utf-8 -*-
"""动态数组
1 插入、删除、按下标随机访问
2 数组中的元素是int类型
@Time   : 2021-02-22 01:43
@Author : Hao
"""

import ctypes


class Array:
    def __init__(self, capacity=4):
        self.capacity = capacity    # 数组容量
        self.data = [0] * capacity
        self.count = 0      # 元素个数
        self.init_capacity = self.capacity

    def find(self, index):
        if index < 0 or index > self.capacity - 1:
            return -1
        return self.data[index]

    def insert(self, index, value):

        if index < 0 or index > self.capacity - 1:
            raise Exception("Index is not valid")

        for i in range(self.count-1,index,-1):
            self.data[i+1] = self.data[i]
        self.data[index] = value
        self.count += 1
        if self.count >= self.capacity:
            self.resize(2 * self.capacity)

    def resize(self, size):

        # tmp = (size * ctypes.py_object)()
        tmp = size * [0]
        for i in range(self.count):
            tmp[i] = self.data[i]
        self.data = tmp
        self.capacity = size

    def add(self, value):
        """尾部添加，满了按2倍扩容"""

        self.data[self.count] = value
        self.count += 1
        if self.count >= self.capacity:
            self.resize(2 * self.capacity)

    def delete(self, index):
        if index < 0 or index >= self.count:
            raise Exception("Index is not valid")
        for i in range(index,self.count,1):
            self.data[i] = self.data[i+1]

        self.count -= 1
        if self.count <= self.capacity//4 and self.capacity//2 != 0 and self.capacity//2 >= self.init_capacity:
            self.resize(self.capacity//2)

    def print_all(self):

        print("[",end='')
        if self.count == 0:
            print("]",end='')
            return
        for i in range(self.count):
            if i != self.count -1:
                print("{0},".format(self.data[i]),end='')
            else:
                print("{0}]".format(self.data[i]),end='')


if __name__ == "__main__":
    arr = Array()
    arr.print_all()
    print(arr.count)
    arr.insert(0,'a')
    arr.insert(1,'b')
    arr.insert(2,'c')
    arr.insert(3,'d')
    print()
    arr.print_all()
    print(arr.count)
    arr.delete(1)
    arr.print_all()
    print(arr.count)
    print('---------')
    arr.insert(3,'e')
    print('count:',arr.count)
    arr.print_all()
    print()
    print('capacity:',arr.capacity)
    print('---------')
    arr.insert(4,'f')
    print('count:',arr.count)
    arr.print_all()
    print()
    print('capacity:', arr.capacity)
    print('---------')
    arr.add('g')
    print('count:',arr.count)
    arr.print_all()
    print()
    print('capacity:', arr.capacity)
    print('---------')
    arr.delete(1)
    arr.delete(1)
    arr.delete(1)
    arr.delete(1)
    arr.delete(1)
    arr.delete(0)
    print('count:', arr.count)
    arr.print_all()
    print()
    print('capacity:', arr.capacity)