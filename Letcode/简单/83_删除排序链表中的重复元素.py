class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        start = head
        while start and start.next:
            if start.val == start.next.val:
                start.next = start.next.next
            else:
                start = start.next