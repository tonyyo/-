class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseStore(self, head):
        ans = []
        self.helper(head, ans)
        return ans
    def helper(self, head, ans):
        if head is None:
            return
        else:
            self.helper(head.next, ans)
        ans.append(head.val)
#主函数
if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3
    list1 = []
    #创建对象
    solution = Solution()
    print("初始链表是：", [node1.val, node2.val, node3.val])
    print("倒序存储到数组中的结果是：", solution.reverseStore(node1))