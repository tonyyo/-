class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        low, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            low  = low.next
            if fast == low:
                return True
        return False