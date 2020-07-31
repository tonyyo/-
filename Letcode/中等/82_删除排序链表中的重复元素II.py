class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        newHead = ListNode(0)
        newHead.next = head
        pre, start = newHead, head
        while start and start.next:
            flag = False
            while start.next and start.val == start.next.val: # 找到最后一个重复的元素
                start.next = start.next.next
                flag = True
            if flag:
                pre.next = start.next
                start = pre.next
            else:
                pre = pre.next
                start = pre.next
        return newHead.next
