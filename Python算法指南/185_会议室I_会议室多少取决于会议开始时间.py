class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
class Solution:
    def minMeetingRooms(self, intervals):
        size = len(intervals)
        point = [] # 存取所有时刻，开始时刻和结束时刻
        for interval in intervals:
            point.append((interval.start, 1))  # 1表示会议室开启
            point.append((interval.end, -1))   # -1表示会议室关闭
        on_MeetingRoom = 0
        max_MeetingRoom = 0
        for _, delta in sorted(point):  # 将所有时间点排好序
            on_MeetingRoom += delta
            max_MeetingRoom = max(on_MeetingRoom, max_MeetingRoom)
        return max_MeetingRoom

#主函数
if __name__ == '__main__':
    node1 = Interval(0, 30)
    node2 = Interval(5, 10)
    node3 = Interval(15, 20)
    intervals = [node1, node2, node3]
    solution = Solution()
    print(solution.minMeetingRooms(intervals))