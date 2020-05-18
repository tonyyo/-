class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
class Solution:
    def hasCycle(self, head):
        if not head or not head.next:
            return False
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False

    def hasCycle1(self, head):
        start = head
        while start:
            start = start.next
            if start == head:
                return True
        return False
#主函数
if __name__ == "__main__":
    node1 = ListNode(-21)
    node2 = ListNode(10)
    node3 = ListNode(4)
    node4 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node3
    # 创建对象
    solution = Solution()
    print("初始化的值是：", [node1.val, node2.val, node3.val, node4.val])
    print("结果是：", solution.hasCycle(node1))