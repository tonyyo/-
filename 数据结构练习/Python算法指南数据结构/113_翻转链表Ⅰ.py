class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse(self, head):
        # curt表示前继节点
        curt = None
        while head != None:
            # temp记录下一个节点，head是当前节点
            temp = head.next
            head.next = curt
            curt = head
            head = temp
        return curt

    def reverse2(self, head):
        newHead = ListNode(0)
        newHead.next = head
        start = head
        while start.next:
            tmp = start.next
            start.next = tmp.next
            tmp.next = newHead.next
            newHead.next = tmp
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

    solution = Solution()
    print("输入的初始链表是：", [node1.val, node2.val, node3.val, node4.val])
    newlist = solution.reverse2(node1)
    while (newlist):
        list1.append(newlist.val)
        newlist = newlist.next
    print("翻转链表后的结果是：", list1)