class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapNodes(self, head, v1, v2):
        dummy = ListNode(0, head)
        cur = dummy
        p1 = None
        p2 = None
        while cur.next != None:
            if cur.next.val == v1:
                p1 = cur
            if cur.next.val == v2:
                p2 = cur
            cur = cur.next
        if p1 is None or p2 is None:
            return dummy.next
        n1 = p1.next
        n2 = p2.next
        n1next = n1.next
        n2next = n2.next
        if p1.next == p2:
            p1.next = n2
            n2.next = n1
            n1.next = n2next
        elif p2.next == p1:
            p2.next = n1
            n1.next = n2
            n2.next = n1next
        else:
            p1.next = n2
            n2.next = n1next
            p2.next = n1
            n1.next = n2next
        return dummy.next

    def swapNodes2(self, head, v1, v2):
        newHead = ListNode(0)
        newHead.next = head
        pre_v1 = newHead
        pre_v2 = newHead
        start = head
        pre_start = newHead
        while start:
            if start.val == v1:
                pre_v1 = pre_start
            if start.val == v2:
                pre_v2 = pre_start
            start = start.next
            pre_start = pre_start.next

        node_v1 = pre_v1.next
        node_v2 = pre_v2.next

        pre_v1.next = node_v1.next

        node_v1.next = node_v2.next
        pre_v2.next = node_v1

        node_v2.next = pre_v1.next
        pre_v1.next = node_v2
        return newHead.next

#主函数
if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    v1 = 2
    v2 = 4
    list1 = []
    #创建对象
    solution = Solution()
    print("初始的链表是：", [node1.val, node2.val, node3.val, node4.val], "初始的两个权值v1=", v1, "v2=", v2)
    newlist = solution.swapNodes2(node1, v1, v2)
    while (newlist):
        list1.append(newlist.val)
        newlist = newlist.next
    print("交换后的链表结果是：", list1)