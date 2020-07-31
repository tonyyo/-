class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        preHead, postHead, start = ListNode(0), ListNode(0), head
        preTail, postTail = preHead, postHead
        while start:
            if start.val < x:
                preTail.next = start
                preTail = preTail.next
            else:
                postTail.next = start
                postTail = postTail.next
            start = start.next
        postTail.next = None
        preTail.next = postHead.next
        return preHead.next

class Solution(object):
    def partition(self, head, x):
        before = before_head = ListNode(0)
        after = after_head = ListNode(0)
        while head:
            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next
            head = head.next
        after.next = None
        before.next = after_head.next
        return before_head.next