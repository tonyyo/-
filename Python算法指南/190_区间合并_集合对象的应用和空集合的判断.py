class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def merge2(self, intervals):
        intervals = sorted(intervals, key=lambda x: x.start)
        result = []
        for interval in intervals:
            if len(result) == 0 or result[-1].end < interval.start:
                result.append(interval)
            else:
                result[-1].end = max(result[-1].end, interval.end)
        return result

    def merge(self, intervals):
        size = len(intervals)
        intervals = sorted(intervals, key = lambda x: x.start)
        result = []
        for interval in intervals:
            if len(result) == 0 or interval.start >= result[-1].end:  # 前面的len专治result为空的情况
                result.append(interval)
            else:
                result[-1].end = interval.end
        return result

# 主函数
if __name__ == "__main__":
    node1 = Interval(1, 3)
    node2 = Interval(2, 6)
    node3 = Interval(8, 10)
    node4 = Interval(15, 18)
    list1 = []
    # 创建对象
    solution = Solution()
    print("初始区间：",
          [(node1.start, node1.end), (node2.start, node2.end), (node3.start, node3.end), (node4.start, node4.end)])
    mind = solution.merge([node1, node2, node3, node4])
    for rement in mind:
        list1.append((rement.start, rement.end))
    print("合并后区间：", list1)
