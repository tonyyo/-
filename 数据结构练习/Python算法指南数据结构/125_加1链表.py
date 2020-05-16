#创建链表
#head的类型是链表节点
#返回值的类型是链表节点
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def plusOne(self, head):
        stack = []
        h = head
        while h:
            stack.append(h)
            h = h.next
        while stack and stack[-1].val == 9:
            stack[-1].val = 0
            stack.pop()
        if stack:
            stack[-1].val += 1
        else:
            node = ListNode(1)
            node.next = head
            head = node
        return head


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
    newlist = solution.plusOne2(node1)
    while (newlist):
        list1.append(newlist.val)
        newlist = newlist.next
    print("最终得到的链表是：", list1)