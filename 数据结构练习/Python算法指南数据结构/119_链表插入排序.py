class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head):
        dummy = ListNode(0)
        while head:
            temp = dummy
            next = head.next
            while temp.next and temp.next.val < head.val:
                temp = temp.next
            head.next = temp.next
            temp.next = head
            head = next
        return dummy.next

    def insertionSortList2(self, head):
        newHead = ListNode(0)
        newHead.next = head
        countStart = newHead
        size = 0
        while countStart.next:
            size += 1
            countStart = countStart.next
        for i in range(size - 1, 0, -1):
            start = newHead
            for _ in range(i - 1):
                start = start.next # 找出一个一个插入的位置的元素
            prestart = start
            start = start.next
            while start.val > start.next.val:
                temp = start.next
                start.next = temp.next
                temp.next = start
                prestart.next = temp
                prestart = prestart.next
                if start.next == None:
                    break
        return newHead.next


#主函数
if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(3)
    node3 = ListNode(2)
    node4 = ListNode(0)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    list1 = []
    #创建对象
    solution = Solution()
    print("初始链表：", [node1.val, node2.val, node3.val, node4.val])
    newlist = solution.insertionSortList2(node1)
    while (newlist):
        list1.append(newlist.val)
        newlist = newlist.next
    print("插入排序后的链表是：", list1)