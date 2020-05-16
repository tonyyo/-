class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
class Solution(object):
    def canAttendMeetings2(self, intervals):
        if len(intervals) == 0:
            return True
        intervals = sorted(intervals, key=lambda x: x.start)
        end = intervals[0].end
        for i in range(1, len(intervals)):
            if end > intervals[i].start:
                return False
            end = intervals[i].end
        return True

    def canAttendMeetings(self, intervals):
        size = len(intervals)
        intervals = sorted(intervals, key = lambda x : x.start)
        end = intervals[0].end
        for i in range(1, size):
            if end > intervals[i].start:
                return False
            end = intervals[i].end
        return True

#主函数
if __name__ == '__main__':
    node1 = Interval(0, 30)
    node2 = Interval(5, 10)
    node3 = Interval(15, 20)
    print("会议时间间隔：", [[node1.start, node1.end], [node2.start, node2.end], [node3.start, node3.end]])
    intervals = [node1, node2, node3]
    solution = Solution()
    print("是否参加所有会议：", solution.canAttendMeetings(intervals))