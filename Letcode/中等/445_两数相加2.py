class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        tail, curNode = None, None
        carry = 0
        if l1.val == 0:
            return l2
        if l2.val == 0:
            return l1
        stack1, stack2 = list(), list()
        while l1:
            stack1.append(l1)
            l1 = l1.next
        while l2:
            stack2.append(l2)
            l2 = l2.next
        while stack1 or stack2 or carry != 0:
            a = stack1.pop().val if stack1 else 0
            b = stack2.pop().val if stack2 else 0
            curSum = a + b + carry
            curVal = curSum % 10
            carry = curSum // 10
            curNode = ListNode(curVal)
            curNode.next = tail
            tail = curNode
        return curNode

