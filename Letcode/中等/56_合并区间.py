class Solution:
    def merge(self, intervals: [[int]]) -> [[int]]:
        if len(intervals) == 0:
            return []
        intervals = sorted(intervals, key=lambda x : (x[0], x[1]))
        result, N = [], len(intervals)
        result.append(intervals[0])
        for i in range(1, N):
            if result[-1][1] >= intervals[i][0]:
                result[-1][1] = intervals[i][1] if intervals[i][1] > result[-1][1] else result[-1][1]
            else:
                result.append(intervals[i])
        return result

