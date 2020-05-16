class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
class Solution:
    def minMeetingRooms2(self, intervals):
        points = []
        for interval in intervals:
            points.append((interval.start, 1))
            points.append((interval.end, -1))
        meeting_rooms = 0
        ongoing_meetings = 0
        for _, delta in sorted(points):
            ongoing_meetings += delta
            meeting_rooms = max(meeting_rooms, ongoing_meetings)
        return meeting_rooms

    def minMeetingRooms(self, intervals):
        size = len(intervals)
        point = [] # 列表里面用元组进行标记时间点, 而不是用字典, 因为时间点可能会重复, 而字典的key不能重复
        for interval in intervals:
            point.append((interval.start, 1))
            point.append((interval.end, -1))
        on_MeetingRoom = 0
        max_MeetingRoom = 0
        for _, delta in sorted(point):
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