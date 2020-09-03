class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head):
        low, fast = head, head
        while True:
            fast = fast.next.next
            low = low.next
            if fast.next == None or fast.next.next == None:
                secHead = low.next
                low.next = None
                break
        secHead = self.reverseList(secHead)
        head1, head2, = head, secHead
        while head1 and head2:
            secHead = secHead.next
            head2.next = head1.next
            head1.next = head2
            head1 = head1.next.next
            head2 = secHead

    def reverseList(self, head):
        if head == None or head.next == None:
            return head
        tail = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return tail

if __name__ == '__main__':
    s = Solution()
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    s.reorderList(node1)