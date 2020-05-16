#参数A是一个整数数组
#返回线段树的根
import collections


class SegmentTreeNode:
    def __init__(self, start, end, max):
        self.start, self.end, self.max = start, end, max
        self.left, self.right = None, None

class Solution:
    def build(self, A):
        return self.buildTree2(0, len(A) - 1, A)

    def buildTree2(self, start, end, A):
        if start == end:
            return SegmentTreeNode(start, end, A[start]) # A中的元素直到遍历到叶子结点才赋值
        node = SegmentTreeNode(start, end, 0)
        node.left = self.buildTree2(start, (start + end)// 2, A) # 采取这样的方法，确定构造多少节点
        node.right = self.buildTree2((start + end) // 2 + 1, end, A)
        node.max = max(node.left.max, node.right.max)  # 重新赋值
        return node



def printTree(root):
    res = []
    if root is None:
        print(res)
    queue = []
    queue.append(root)
    while len(queue) != 0:
        tmp = []
        length = len(queue)
        for i in range(length):
            r = queue.pop(0)
            if r.left is not None:
                queue.append(r.left)
            if r.right is not None:
                queue.append(r.right)
            tmp.append(r.max)
        res.append(tmp)
    print(res)
if __name__ == '__main__':
    A = [3, 2, 1, 4]
    print("输入的数组是：", A)
    solution = Solution()
    root = solution.build(A)
    print("构造的线段树是：")
    printTree(root)