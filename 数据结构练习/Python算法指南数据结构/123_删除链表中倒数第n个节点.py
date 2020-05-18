class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        res = ListNode(0)
        res.next = head
        tmp = res
        for i in range(0, n):
            head = head.next
        while head != None:
            head = head.next
            tmp = tmp.next
        tmp.next = tmp.next.next
        return res.next

    def removeNthFromEnd2(self, head, n):
        newHead = ListNode(0)
        newHead.next = head
        pre_slow = newHead
        slow = head
        fast = head
        for _ in range(n - 1):
            fast = fast.next
        while fast.next:
            fast = fast.next
            pre_slow = pre_slow.next
            slow = slow.next
        pre_slow.next = slow.next
        return newHead.next

#主函数
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
    list1 = []
    n = 1
    #创建对象
    solution = Solution()
    print("初始链表是：", [node1.val, node2.val, node3.val, node4.val, node5.val])
    newlist = solution.removeNthFromEnd2(node1, n)
    while (newlist):
        list1.append(newlist.val)
        newlist = newlist.next
    print("最终链表是：", list1)