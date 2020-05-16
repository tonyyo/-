class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head, m, n):
        if head is None:
            return
        sub_vals = []  # contain the vals from m to n
        dummy = ListNode(0, head)
        fake_head = dummy
        i = 0
        while fake_head:
            # find the m - 1 node
            if i == m - 1:
                cur = fake_head.next
                j = i + 1
                # extract the values of the nodes ranged from m to n
                while j >= m and j <= n:
                    # print(cur.val)
                    sub_vals.append(cur.val)
                    cur = cur.next
                    j += 1
                    # build up reversed linked list
                sub_vals.reverse()
                sub_head = ListNode(sub_vals[0])
                sub_dummy = ListNode(0, sub_head)
                for val in sub_vals[1:]:
                    node = ListNode(val)
                    sub_head.next = node
                    sub_head = sub_head.next
                    # relink the original list to the sub list
                fake_head.next = sub_dummy.next
                sub_head.next = cur
            fake_head = fake_head.next
            i += 1
        return dummy.next

    def reverseBetween2(self, head, m, n):
        newHead = ListNode(0)
        newHead.next = head
        start = newHead
        for _ in range(m - 1):
            start = start.next
        rootStart = start
        start = start.next
        for _ in range(n - m):
            tmp = start.next
            start.next = tmp.next
            tmp.next = rootStart.next
            rootStart.next = tmp
        return newHead


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
    m = 2
    n = 4

    solution = Solution()
    print("初始链表是：", [node1.val, node2.val, node3.val, node4.val, node5.val], "初始的m=", m, "n=", n)
    newlist = solution.reverseBetween2(node1, m, n)
    while (newlist):
        list1.append(newlist.val)
        newlist = newlist.next
    print("翻转后的链表是：", list1)