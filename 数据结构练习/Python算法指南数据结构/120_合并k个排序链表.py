# ListNode的定义
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: [ListNode]) -> ListNode: # 合并k个排序链表
        if len(lists) == 0:
            return None
        left, right = 0, len(lists) - 1
        return self.mergeK(lists, left, right)

    def mergeK(self, lists, left, right):  # 合并list从left到right的有序链表，并返回合并好链表的头节点
        if left == right:
            return lists[left]
        mid = (left + right) // 2
        leftNode = self.mergeK(lists, left, mid)
        rightNode = self.mergeK(lists, mid + 1, right)
        return self.merge(leftNode, rightNode)

    def merge(self, leftNode, rightNode):
        if not leftNode:
            return rightNode
        if not rightNode:
            return leftNode
        if leftNode.val < rightNode.val:
            leftNode.next = self.merge(leftNode.next, rightNode)
            return leftNode
        else:
            rightNode.next = self.merge(leftNode, rightNode.next)
            return rightNode

    #打印链表函数
    def printlist(self, node):
        out = []
        if node is None:
            print(out)
        while node.next is not None:
            out.append(node.val)
            node = node.next
        out.append(node.val)
        print(out)
#主函数
if __name__ == '__main__':
    node1 = ListNode(2)
    node2 = ListNode(4)
    node3 = ListNode(-1)
    node4 = ListNode(5)
    node1.next = node2
    #创建对象
    solution = Solution()
    A = [node1, node3, node4]
    print("排序后的链表是：", end="")
    solution.printlist(solution.mergeKLists(A))