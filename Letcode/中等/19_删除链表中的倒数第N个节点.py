class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast, low = head, head
        for i in range(n):
            fast = fast.next
        if fast == None:
            head = head.next
            return head
        while fast and fast.next:
            fast = fast.next
            low = low.next
        low.next = low.next.next
        return head