class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head, val):
        if head == None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        while head:
            if head.val == val:
                pre.next = head.next
                head = pre
            pre = head
            head = head.next
        return dummy.next
        # 主函数

    def removeElements2(self, head, val):
        newHead = ListNode(0)
        newHead.next = head
        pre_start = newHead
        start = head
        while start:  # 这里最好用start， 而不是start.next, 不然就算跳出循环你也判断最后一个数的情况
            if start.val == val:
                pre_start.next = start.next
                start = pre_start.next
            else:
                pre_start = pre_start.next
                start = start.next
        return newHead.next

if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(3)
    node5 = ListNode(4)
    node6 = ListNode(5)
    node7 = ListNode(3)
    node1.next=node2
    node2.next=node3
    node3.next=node4
    node4.next=node5
    node5.next=node6
    node6.next=node7
    val = 3
    list1 = []
    # 创建对象
    solution = Solution()
    print("初始链表是：", [node1.val, node2.val, node3.val, node4.val, node5.val, node6.val, node7.val], "需要被删除的节点val=", val)
    newlist = solution.removeElements2(node1, val)
    while (newlist):
        list1.append(newlist.val)
        newlist = newlist.next
    print("删除指定节点后的链表是：", list1)