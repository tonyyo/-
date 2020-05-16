class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head, k):
        if head == None:
            return head
        curNode = head
        size = 1
        while curNode != None:
            size += 1
            curNode = curNode.next
        size -= 1
        k = k % size
        if k == 0:
            return head
        len = 1
        curNode = head
        while len < size - k:
            len += 1
            curNode = curNode.next
        newHead = curNode.next
        curNode.next = None
        curNode = newHead
        while curNode.next != None:
            curNode = curNode.next
        curNode.next = head
        return newHead

    def rotateRight2(self, head, k):
        newHead = ListNode(0)
        newHead.next = head
        start = newHead
        size = 0
        while start.next:
            size += 1
            start = start.next
        rightEnd = start
        start2 = newHead
        for _ in range(size - k):
            start2 = start2.next
        rightStart = start2.next
        start2.next = None
        newHead.next = rightStart
        rightEnd.next = head
        return  newHead.next

if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    k = 2
    list1 = []

    solution = Solution()
    print("初始链表：", [node1.val, node2.val, node3.val, node4.val, node5.val],"初始的k=",k)
    newlist = solution.rotateRight2(node1, k)
    while (newlist):
        list1.append(newlist.val)
        newlist = newlist.next
    print("旋转后的链表是：", list1)