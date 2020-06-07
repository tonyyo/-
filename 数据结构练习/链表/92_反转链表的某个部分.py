class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        newHead = ListNode(-1)
        newHead.next = head
        pre = newHead
        cur = head
        index = 1
        prefix = None
        while cur:
            if index == m:
                prefix = pre
            if index > m and index <= n:
                pre.next = cur.next
                cur.next = prefix.next
                prefix.next = cur
                cur = pre.next
                if index == n:
                    return newHead.next
                index += 1
                continue
            pre = pre.next
            cur = cur.next
            index += 1
        return newHead.next # 如果m是头节点，那么就直接返回cur

    def printList(self, head):
        while head:
            print(head.val, end=" ")
            head = head.next

if __name__ == '__main__':
    solution = Solution()
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    solution.printList(solution.reverseBetween(node1, 1, 4))