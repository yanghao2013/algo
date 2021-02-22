# -*- coding: utf-8 -*-
"""动态数组
1 插入、删除、按下标随机访问
2 数组中的元素是int类型
@Time   : 2021-02-22 01:43
@Author : Hao
"""


class Array:
    def __init__(self, capacity):
        self.capacity = capacity    # 数组容量
        self.data = [0] * capacity
        self.count = 0      # 元素个数

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

    def add(self, value):
        """添加，满了按2倍扩容"""
        pass

    def delete(self, index):
        if index < 0 or index >= self.count:
            raise Exception("Index is not valid")
        for i in range(index,self.count,1):
            self.data[i] = self.data[i+1]

        # todo 缩容
        self.count -= 1

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
    arr = Array(10)
    arr.print_all()
    print(arr.count)
    arr.insert(0,'a')
    arr.insert(2,'b')
    arr.insert(1,'c')
    arr.insert(3,'d')
    print()
    arr.print_all()
    print(arr.count)
    arr.delete(1)
    arr.print_all()
    print(arr.count)