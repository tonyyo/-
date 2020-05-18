class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head):
        if None == head or None == head.next:
            return head
        pfast = head
        pslow = head
        while pfast.next and pfast.next.next:
            pfast = pfast.next.next
            pslow = pslow.next
        pfast = pslow.next
        pslow.next = None
        pnext = pfast.next
        pfast.next = None
        while pnext:
            q = pnext.next
            pnext.next = pfast
            pfast = pnext
            pnext = q
        tail = head
        while pfast:
            pnext = pfast.next
            pfast.next = tail.next
            tail.next = pfast
            tail = tail.next.next
            pfast = pnext
        return head

    def reorderList2(self, head):
        newHead = ListNode(0)
        newHead.next = head
        start = head
        while start.next.next:
            start = start.next
        last = start.next
        start.next = None
        last.next = head.next
        head.next = last
        return newHead.next

#主函数
if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    list1 = []
    #创建对象
    solution = Solution()
    print("初始链表：", [node1.val, node2.val, node3.val, node4.val])
    newlist = solution.reorderList2(node1)
    while (newlist):
        list1.append(newlist.val)
        newlist = newlist.next
    print("重排后的链表是：", list1)