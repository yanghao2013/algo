# -*- coding: utf-8 -*-
"""单链表实现
1. 插入、删除、查找操作
2. 链表中存储的int类型数据
@Time   : 2021-02-22 00:16
@Author : Hao
"""


class SinglyLinkedList:
    class Node:
        def __init__(self, data=None):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None

    def find_by_value(self, value):
        if not self.head:
            return None
        cur = self.head
        while cur:
            if cur.value == value:
                return cur
            cur = cur.next
        return None

    def find_by_index(self, index):
        if not self.head:
            return -1
        cur = self.head
        count = 0
        while cur:
            count += 1
            if count == index:
                return cur
            cur = cur.next
        return -1

    def insert_to_head(self, value):
        """表头插入，无头节点逆序插入"""
        new_node = SinglyLinkedList.Node(value)
        if not self.head:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def insert_to_tail(self, value):
        """表尾插入，无头节点顺序插入"""
        new_node = SinglyLinkedList.Node(value)
        if not self.head:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def insert_to_head_with_dummy_node(self, value):
        """表头插入，有哨兵头节点逆序插入"""
        dummy_node = SinglyLinkedList.Node()
        new_node = SinglyLinkedList.Node(value)
        new_node.next = dummy_node.next
        dummy_node.next = new_node

    def insert_to_tail_dummy_node(self, value):
        """表尾插入，有哨兵节点顺序插入"""
        dummy_node = SinglyLinkedList.Node()
        new_node = SinglyLinkedList.Node(value)
        cur = dummy_node
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def insert_before(self, p, value):
        """插入到p节点之前"""
        # find p
        dummy_node = SinglyLinkedList.Node()
        new_node = SinglyLinkedList.Node(value)
        cur = dummy_node
        while cur.next:
            if cur.next.data == p.data:
                new_node.next = cur.next
                cur = new_node
                break
            cur = cur.next
        raise Exception("Can not find p, please check!")

    def insert_after(self, p, value):
        """插入到p节点之后"""
        dummy_node = SinglyLinkedList.Node()
        new_node = SinglyLinkedList.Node(value)
        cur = dummy_node.next
        while cur:
            if cur.data == p.data:
                if not cur.next:
                    cur.next = new_node
                else:
                    new_node.next = cur.next
                    cur = new_node
                break
            cur = cur.next
        raise Exception("Can not find p, please check!")

    def delete_by_node(self, p):
        dummy_node = SinglyLinkedList.Node()
        cur = dummy_node
        while cur.next:
            if cur.next.data == p.value:
                cur.next = cur.next.next
            cur = cur.next
        raise Exception("Can not find p, please check!")

    def delete_by_value(self, value):
        dummy_node = SinglyLinkedList.Node()
        cur = dummy_node
        while cur.next:
            if cur.next.data == value:
                cur.next = cur.next.next
            cur = cur.next
        raise Exception("Can not find p, please check!")

    def print_all(self):
        dummy_node = SinglyLinkedList.Node()
        dummy_node.next = self.head
        cur = dummy_node
        print("[",end='')
        while cur.next:
            if cur.next.next:
                print(cur.next.data,end=',')
            else:
                print(cur.next.data,end='')
            cur = cur.next
        print("]",end='')

    def is_palindrome(self):
        """判断是否回文"""
        # find middle
        if not self.head:
            return False
        tmp = self.head
        p = self.head
        q = self.head
        if not p.next:
            return True
        while q.next and q.next.next:
            p = p.next
            q = q.next.next
        first_half_end = p
        second_half_start = self.inverse_linked_list_with_dummy_node(first_half_end.next)

        # reverse right linklist
        first_position = self.head
        second_position = second_half_start
        # compare left and right list
        result = True
        while result and second_position:
            if first_position.data != second_position.data:
                result = False
                break
            second_position = second_position.next
            first_position = first_position.next
        # 还原链表并返回结果
        p.next = self.inverse_linked_list_with_dummy_node(second_half_start)
        self.head = tmp
        return result

    def inverse_linked_list_with_dummy_node(self, p):
        """从任意节点反转后半段"""
        self.head = p
        if self.head is None:
            return
        cur = self.head
        last = None # 存储前一个节点指针
        while cur:
            tmp = cur.next
            cur.next = last
            last = cur
            cur = tmp
        self.head = last
        return last

    def inverse_linked_list_by_recuise(self):
        """递归方式反转链表"""
        pass

    def inverse_linked_list(self):
        """无头节点的链表反转"""
        pass


if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.insert_to_head(1)
    sll.insert_to_head(2)
    sll.insert_to_head(3)
    sll.insert_to_head(2)
    sll.insert_to_head(1)
    sll.print_all()
    # sll.inverse_linked_list_with_dummy_node(sll.head)
    res = sll.is_palindrome()
    print(res)
    sll.print_all()
