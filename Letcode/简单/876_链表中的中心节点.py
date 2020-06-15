class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        fast, low = head, head
        while fast and fast.next:
            fast = fast.next.next
            low = low.next
        return low