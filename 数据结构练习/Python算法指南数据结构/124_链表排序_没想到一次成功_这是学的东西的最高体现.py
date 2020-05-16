class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeSort(self, head):
        midHead = self.findMidNode(head)
        if midHead == head:    # 当链表中只有一个元素时返回它
            return head
        leftHead = self.mergeSort(head)
        rightHead = self.mergeSort(midHead)
        return self.merge(leftHead, rightHead)

    def findMidNode(self, head):
        size = 0
        newHead = ListNode(0)
        newHead.next = head
        start = head
        mid = head
        premid = newHead
        while start:
            size += 1
            start = start.next
        for _ in range(size//2):
            premid = premid.next
            mid = mid.next
        premid.next = None  # 切断左右链表
        return mid

    def merge(self, head1, head2):
        newHead = ListNode(0)
        start = newHead
        start1 = head1
        start2 = head2
        while start1 and start2:
            if start1.val >= start2.val:
                start.next = start2
                start = start.next
                start2 = start2.next
            else:
                start.next = start1
                start = start.next
                start1 = start1.next
        while start1:
            start.next = start1
            start1 = start1.next
            start = start.next
        while start2:
            start.next = start2
            start2 = start2.next
            start = start.next
        return newHead.next

#主函数
if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(3)
    node3 = ListNode(2)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(0)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    list1 = []
    #创建对象
    solution = Solution()
    newlist = solution.mergeSort(node1)
    while (newlist):
        list1.append(newlist.val)
        newlist = newlist.next
    print("排序后的链表：", list1)