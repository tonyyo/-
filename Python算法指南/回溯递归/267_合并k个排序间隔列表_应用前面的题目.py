class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def mergeKSortedIntervalLists1(self, intervals):
        data = []
        for i in intervals:
            data += i
        data.sort(key=lambda t: t.start)
        res = [data[0]]
        for d in data:
            if res[-1].end < d.start:
                res += [d]
            else:
                res[-1].end = max(res[-1].end, d.end)
        return res

    def mergeKSortedIntervalLists(self, intervals):
        merge = []
        result = []
        for i in range(len(intervals)):
            for j in range(len(intervals[i])):
                merge.append(intervals[i][j])
        merge = sorted(merge, key = lambda x : (x.start, x.end))
        for i in range(1, len(merge)):
            if result == [] or result[-1].end < merge[i].start:
                result.append(merge[i])
            else:
                result[-1].end = merge[i].end
        return result


if __name__ == '__main__':
    a = Interval(1, 3)
    b = Interval(4, 7)
    c = Interval(6, 8)
    d = Interval(1, 2)
    e = Interval(9, 10)
    intervals0 = [[a, b, c], [d, e]]
    solution = Solution()
    intervals = solution.mergeKSortedIntervalLists(intervals0)
    print("合并重叠的间隔：")
    for interval in intervals:
        print("(", interval.start, ",", interval.end, ")")
