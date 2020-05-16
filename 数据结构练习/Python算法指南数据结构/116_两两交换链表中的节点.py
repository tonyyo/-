class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        temp = head.next
        head.next = self.swapPairs(head.next.next)  # 从后往前交换
        temp.next = head
        return temp

    def swapPairs2(self, head):
        newHead = ListNode(0)
        newHead.next = head
        pre_start = head
        start = head.next
        while pre_start.next:
            pre_start.val, start.val = start.val, pre_start.val
            pre_start = start.next
            if pre_start is None:
                return newHead.next
            start = pre_start.next
        return newHead.next

if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    list1 = []
    #创建对象
    solution = Solution()
    print("初始链表是：", [node1.val, node2.val, node3.val, node4.val])
    newlist = solution.swapPairs2(node1)
    while (newlist):
        list1.append(newlist.val)
        newlist = newlist.next
    print("交换后的链表是：", list1)