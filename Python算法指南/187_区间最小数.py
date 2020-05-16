class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
class SegmentTree(object):
    def __init__(self, start, end, min=0):
        self.start = start
        self.end = end
        self.min = min
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
        node.min = min(node.left.min, node.right.min)
        return node
    @classmethod
    def query(self, root, start, end):
        if root.start > end or root.end < start:
            return 0x7fffff
        if start <= root.start and root.end <= end:
            return root.min
        return min(self.query(root.left, start, end), \
                   self.query(root.right, start, end))
class Solution:
    """
   参数A、queries是一个给定的整数数组和一个间隔列表，第i个查询是[queries[i-1].start, queries[i-1].end]，返回结果列表
    """
    def intervalMinNumber2(self, A, queries):
        root = SegmentTree.build(0, len(A) - 1, A)
        result = []
        for query in queries:
            result.append(SegmentTree.query(root, query.start, query.end))
        return result

    def intervalMinNumber(self, A, queries):
        ans = []
        sizeA = len(A)
        sizeQ = len(queries)
        for q in queries:
            ans.append(min(A[q.start : q.end + 1]))
        return ans
#主函数
if __name__ == '__main__':
    A = [1, 2, 7, 8, 5]
    print("输入的数组是：", A)
    interval1 = Interval(1, 2)
    interval2 = Interval(0, 4)
    interval3 = Interval(2, 4)
    print("要查询的区间为：(", interval1.start, ",", interval1.end, "),(", interval2.start, ",", interval2.end, "),(",
          interval3.start, ",", interval3.end, ")")
    solution = Solution()
    print("区间最小数是：", solution.intervalMinNumber(A, [interval1, interval2, interval3]))