class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        pre = None
        curr = head
        while curr:
            if pre == None:
                if curr.val == val:
                    head = head.next
                    curr = head  # pre节点不动
                else:
                    pre = curr
                    curr = curr.next
            else:
                if curr.val == val:
                    pre.next = curr.next
                    curr = curr.next  # pre节点不动
                else:
                    pre = curr
                    curr = curr.next
        return head
