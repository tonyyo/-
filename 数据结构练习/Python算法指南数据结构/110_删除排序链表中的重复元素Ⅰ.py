class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head):
        if None == head or None == head.next:
            return head
        new_head = ListNode(-1)
        new_head.next = head
        parent = new_head
        cur = head
        while None != cur and None != cur.next:  ### check cur.next None
            if cur.val == cur.next.val:
                val = cur.val
                while None != cur and val == cur.val:  ### check cur None
                    cur = cur.next
                parent.next = cur
            else:
                cur = cur.next
                parent = parent.next
        return new_head.next

    def deleteDuplicates2(self, head):
        newHead = ListNode(0)
        newHead.next = head
        start = head
        prestart = newHead
        flag = False
        while start:
            if start.next == None:
                return newHead.next
            while start.val == start.next.val:
                start = start.next
                flag = True  # 神来之笔
            if flag:
                prestart.next = start.next
                flag = False
            prestart = start
            start = start.next
        return newHead.next


if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(1)
    node3 = ListNode(2)
    node4 = ListNode(3)
    node5 = ListNode(3)
    node6 = ListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    list1 = []

    solution = Solution()
    print("初始链表：", [node1.val, node2.val, node3.val, node4.val, node5.val])
    newlist = solution.deleteDuplicates2(node1)
    while (newlist):
        list1.append(newlist.val)
        newlist = newlist.next
    print("删除重复元素后的结果是：", list1)
