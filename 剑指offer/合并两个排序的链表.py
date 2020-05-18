# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        newHead = ListNode(0)
        start1, start2 = pHead1,pHead2
        start = newHead                 # 三个指针，一个指向新链表尾部，两个指向旧链表。
        if start1.val > start2.val:
            newHead.next = start2
            start2 = start2.next
        else:
            newHead.next = start1
            start1 = start1.next
        start = start.next              # 更新尾部指针
        while start1 and start2:
            if start1.val > start2.val:
                start.next = start2
                start2 = start2.next
            else:
                start.next = start1
                start1 = start1.next
            start = start.next          # 更新尾部指针
        while start1:
            start.next = start1
            start1 = start1.next
            start = start.next          # 更新尾部指针
        while start2:
            start.next = start2
            start2 = start2.next
            start = start.next          # 更新尾部指针
        return newHead.next

