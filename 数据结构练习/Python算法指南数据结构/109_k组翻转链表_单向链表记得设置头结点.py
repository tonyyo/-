class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverse(self, start, end):
        newHead = ListNode(0) # 做链表题时首先定义一个头节点，指向链表
        newHead.next = start
        preStart = newHead   # 如果要交换位置，那么就需要定义一个前指针，用于start向后移动时，不断进行交换位置。
        while start.next != end:  # start一直往后走，直到找到end
            temp = start.next
            start.next = temp.next
            temp.next = preStart.next
            preStart.next = temp
            preStart = temp
        end = start.next   # 找到end后， 将end放到头节点
        start.next = end.next
        end.next = newHead.next
        newHead.next = end
        return [newHead.next, start] # 返回翻转后的链表的头结点和下一个范围的起始点的前驱

    def reverseKGroup(self, head, k):
        newHead = ListNode(0)
        newHead.next = head
        start = newHead   # 因为要接着下一个翻转链表
        while start.next:
            end = start # end是基于start开始往后算的，除了第一个start是头结点，后续的头结点都是程序过程中记录的
            for i in range(k):
                end = end.next
                if end == None: # 当不满足k个数时，结束翻转
                    return newHead.next
            print(start.next.val, end.val)
            doneHead, nextStart = self.reverse(start.next, end) # 注意，你这里应该传入的是start.next，也就是翻转链表的头
            start.next = doneHead
            start = nextStart  # 下一个翻转链表的前驱
        return newHead.next

#主函数
if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    k = 4
    list1 = []
    #创建对象
    solution = Solution()
    newlist = solution.reverseKGroup(node1, k)
    while (newlist):
        list1.append(newlist.val)
        newlist = newlist.next
    print("初始化的链表是：", [node1.val, node2.val, node3.val, node4.val, node5.val])
    print(" 翻转后的结果是:", list1)