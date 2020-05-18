class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
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
    def query(self, root, start, end):
        if root.start > end or root.end < start:
            return 0
        if start <= root.start and root.end <= end:
            return root.sum
        return self.query(root.left, start, end) + \
               self.query(root.right, start, end)
class Solution:
#参数A、queries是给定的一个整数数组和一个区间列表
#第i个查询是[queries[i-1].start, queries[i-1].end]
#返回结果列表
    def intervalSum(self, A, queries):
        root = SegmentTree.build(0, len(A) - 1, A)
        result = []
        for query in queries:
            result.append(SegmentTree.query(root, query.start, query.end))
        return result
if __name__ == '__main__':
    A = [1, 2, 7, 8, 5]
    print("输入的数组是", A)
    interval1 = Interval(1, 2)
    interval2 = Interval(0, 4)
    interval3 = Interval(2, 4)
    print("要查询的区间为：(", interval1.start, ",", interval1.end, "),(", interval2.start, ",", interval2.end, "),(",
          interval3.start, ",", interval3.end, ")")
    solution = Solution()
    print("区间求和：", solution.intervalSum(A, [interval1, interval2, interval3]))