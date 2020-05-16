class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head, x):
        if head is None:
            return head
        aHead, bHead = ListNode(0), ListNode(0)
        aTail, bTail = aHead, bHead
        while head is not None:
            if head.val < x:
                aTail.next = head
                aTail = aTail.next
            else:
                bTail.next = head
                bTail = bTail.next
            head = head.next
        bTail.next = None
        aTail.next = bHead.next
        return aHead.next

    def partition2(self, head, x):
        newHead = ListNode(0)
        midNode = ListNode(x)
        start = head
        left = newHead
        right = midNode
        while start:
            if start.val < midNode.val:
                left.next = start
                left = left.next
            elif start.val  >= midNode.val:
                right.next = start
                right = right.next
            start = start.next

        left.next = midNode.next
        right.next = None  # right 后面还有东西，要置为None
        return newHead.next

if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(4)
    node3 = ListNode(3)
    node4 = ListNode(2)
    node5 = ListNode(5)
    node6 = ListNode(2)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    list1 = []
    x = 3

    solution = Solution()
    print("初始链表：", [node1.val, node2.val, node3.val, node4.val, node5.val, node6.val])
    newlist = solution.partition2(node1, 3)
    while (newlist):
        list1.append(newlist.val)
        newlist = newlist.next
    print("最终的链表是：", list1)