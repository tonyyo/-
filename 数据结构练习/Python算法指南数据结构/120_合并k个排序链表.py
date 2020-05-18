# ListNode的定义
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
class Solution:
    def merge(self, head1, head2):
        newHead = ListNode(0)
        start = newHead
        while head1 and head2:
            if head1.val >= head2.val:
                start.next = head2
                start = start.next
                head2 = head2.next
            else:
                start.next = head1
                start = start.next
                head1 = head1.next
        while head1:
            start.next = head1
            start = start.next
            head1 = head1.next
        while head2:
            start.next = head2
            start = start.next
            head2 = head2.next
        return newHead.next

    def mergeKList(self, List):
        tempHead = List[0]
        for i in range(1, len(List)):
            tempHead = self.merge(tempHead, List[i])
        return tempHead

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
    solution.printlist(solution.mergeKList(A))