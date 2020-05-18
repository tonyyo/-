class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome2(self, head):
        if head is None:
            return True
        fast = slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        p, last = slow.next, None
        while p:
            next = p.next
            p.next = last
            last, p = p, next
        p1, p2 = last, head
        while p1 and p1.val == p2.val:
            p1, p2 = p1.next, p2.next
        p, last = last, None
        while p:
            next = p.next
            p.next = last
            last, p = p, next
            slow.next = last
        return p1 is None

    def isPalindrome(self, head):
        string = ""
        p = node1
        while p:
            val = p.val
            string = string + str(val)
            p = p.next
        if string == string[::-1]:
            return True
        return False


# 主函数
if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(2)
    node4 = ListNode(1)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    solution = Solution()
    print(solution.isPalindrome(node1))
