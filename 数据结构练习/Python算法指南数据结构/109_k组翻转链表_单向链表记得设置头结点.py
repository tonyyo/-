class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverse(self, start, end):
        newHead = ListNode(0) # 做链表题时首先定义一个头节点，指向链表
        newHead.next = start
        while start.next != end:  # start一直往后走，直到找到end
            temp = start.next
            start.next = temp.next
            temp.next = newHead.next
            newHead.next = temp
        start.next = end.next   # 找到end节点后，将其置于头节点
        end.next = newHead.next
        newHead.next = end
        return newHead.next, start # 返回翻转后的链表的头结点和下一个范围的起始点的前驱

    def reverseKGroup(self, head, k):
        if k == 1:
            return head
        newHead = ListNode(0)
        newHead.next = head
        start = newHead # 好计算k个链表节点以及衔接翻转好的链表
        while start.next:
            end = start # end是基于start开始往后算的
            for i in range(k):
                end = end.next
                if end == None: # 当不满足k个数时，结束翻转
                    return newHead.next
            doneHead, nextStart = self.reverse(start.next, end)
            start.next = doneHead
            start = nextStart  # 下一个翻转链表的前驱节点
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
    k = 1
    list1 = []
    #创建对象
    solution = Solution()
    newlist = solution.reverseKGroup(node1, k)
    while (newlist):
        list1.append(newlist.val)
        newlist = newlist.next
    print("初始化的链表是：", [node1.val, node2.val, node3.val, node4.val, node5.val])
    print(" 翻转后的结果是:", list1)