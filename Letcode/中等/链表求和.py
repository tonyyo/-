class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        newHead, carry = ListNode(0), 0
        start = newHead
        while l1 or l2 or carry:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            cur = (a + b + carry) % 10
            carry = (a + b + carry) // 10
            start.next = ListNode(cur)
            start = start.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return newHead.next