class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            tempNext = curr.next
            if prev == None:
                curr.next = None
            else:
                curr.next = prev
            prev = curr
            curr = tempNext
        return prev
