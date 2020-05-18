class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head):
        delflag = 1
        flag = 1
        p = head
        while (p != None and p.next != None):
            if p.val != p.next.val:
                flag = 1
                p = p.next
            elif flag < delflag:
                flag += 1
                p = p.next
            else:
                p.next = p.next.next
        return head

    def deleteDuplicates2(self, head):
        newHead = ListNode(0)
        newHead.next = head
        nonDupList = []
        start = head
        prestart = newHead
        while start:
            if start.val not in nonDupList:
                nonDupList.append(start.val)
                prestart = start
                start = start.next
            else:
                prestart.next = start.next
                start = prestart.next

        return newHead.next

if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(1)
    node3 = ListNode(2)
    node1.next = node2
    node2.next = node3
    list1 = []

    solution = Solution()
    print("初始链表是：", [node1.val, node2.val, node3.val])
    newlist = solution.deleteDuplicates2(node1)
    while (newlist):
        list1.append(newlist.val)
        newlist = newlist.next
    print("删除重复元素后的链表：", list1)