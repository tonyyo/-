class SegmentTreeNode:
    def __init__(self, start, end, max):
        self.start, self.end, self.max = start, end, max
        self.left, self.right = None, None
class SegmentTree(object):
    def __init__(self, start, end, sum=0):
        self.start = start
        self.end = end
        self.sum = sum
        self.left, self.right = None, None
    @classmethod
    def build(cls, start, end, a):
        if start > end:
            return None
        if start == end:
            return SegmentTree(start, end, a[start])
        node = SegmentTree(start, end, a[start])
        mid = (start + end) // 2
        node.left = cls.build(start, mid, a)
        node.right = cls.build(mid + 1, end, a)
        node.sum = node.left.sum + node.right.sum
        return node
    @classmethod
    def modify(cls, root, index, value):
        if root is None:
            return
        if root.start == root.end:
            root.sum = value
            return
        if root.left.end >= index:
            cls.modify(root.left, index, value)
        else:
            cls.modify(root.right, index, value)
        root.sum = root.left.sum + root.right.sum
    @classmethod
    def query(cls, root, start, end):
        if root.start > end or root.end < start:
            return 0
        if start <= root.start and root.end <= end:
            return root.sum
        return cls.query(root.left, start, end) + \
               cls.query(root.right, start, end)
class Solution:
    # 参数A是整数序列
    def __init__(self, A):
        #
        self.root = SegmentTree.build(0, len(A) - 1, A)
    #参数start和end是索引
    #返回值是从start到end的和
    def query(self, start, end):
         return SegmentTree.query(self.root, start, end)
    #参数index、value是将A[index]修改为value
    def modify(self, index, value):
         SegmentTree.modify(self.root, index, value)
if __name__ == '__main__':
    A = [1, 2, 7, 8, 5]
    print("输入的数组是：", A)
    solution = Solution(A)
    solution.__init__(A)
    print("运行query(0,2)：", solution.query(0, 2))
    print("运行modify(0,4)")
    solution.modify(0, 4)
    print("运行query(0,1)：", solution.query(0, 1))
    print("运行modify(2,1)")
    solution.modify(2, 1)
    print("运行query(2,3)：", solution.query(2, 4))