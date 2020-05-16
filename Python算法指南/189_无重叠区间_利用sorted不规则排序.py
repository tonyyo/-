# 采用utf-8编码格式
import sys


class Solution:
    def eraseOverlapIntervals2(self, intervals):
        ans = 0
        end = -sys.maxsize
        for i in sorted(intervals, key=lambda i: i[-1]):
            if i[0] >= end:
                end = i[-1]
            else:
                ans += 1
        return ans

    def eraseOverlapIntervals(self, intervals):
        size = len(intervals)
        intervals = sorted(intervals, key = lambda x: x[-1])
        end = intervals[0][1]
        count = 0
        for i in range(1, size):
            if end > intervals[i][0]:
                count += 1
                continue
            else:
                end = intervals[i][1]
        return count

if __name__ == '__main__':
    temp = Solution()
    List1 = [[1, 2], [2, 3], [3, 4], [1, 3]]
    List2 = [[1, 2], [1, 2], [1, 2]]
    print(("输入：" + str(List1)))
    print(("输出：" + str(temp.eraseOverlapIntervals(List1))))
    print(("输入：" + str(str(List2))))
    print(("输出：" + str(temp.eraseOverlapIntervals(List2))))
