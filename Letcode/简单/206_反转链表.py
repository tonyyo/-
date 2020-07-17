class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:  # 反转链表，并返回原链表尾节点
        if head == None or head.next == None: return head
        tail = self.reverseList(head.next)
        head.next.next = head
        head.next = None    # 切记， 不然会形成循环链表
        return tail



    def reverseList2(self, head: ListNode) -> ListNode:  # 迭代
        newHead = ListNode(0)
        newHead.next = head
        start = head
        while start and start.next: # start只能到最后一个元素，不能到None
            temp = start.next
            start.next = temp.next
            temp.next = newHead.next
            newHead.next = temp
        return newHead.next