class Solution(object):
    def shortestDistance(self, maze, start, destination):
        if maze is None or len(maze) == 0 or len(maze[0]) == 0:
            return -1
        marked = set()
        dist_to = {}
        pq = IndexPriorityQueue()
        x, y = start
        pq.push((x, y), 0)
        while pq.size() != 0:
            (x, y), dist = pq.pop()
            if x == destination[0] and y == destination[1]:
                return dist
            self.relaxVertex(maze, marked, pq, x, y, dist)
        return -1
    def relaxVertex(self, maze, marked, pq, x, y, dist):
        marked.add((x, y))
        for key, next_dist in self.nextSpaces(maze, x, y, dist):
            if key in marked:
                continue
            if pq.contains(key):
                if pq.getDistance(key) > next_dist:
                    pq.change(key, next_dist)
            else:
                pq.push(key, next_dist)
    def nextSpaces(self, maze, x, y, dist):
        next_spaces = []
        vectors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for v in vectors:
            next_x, next_y = x, y
            next_dist = dist
            while self.isSpace(maze, next_x + v[0], next_y + v[1]):
                next_x, next_y = next_x + v[0], next_y + v[1]
                next_dist += 1
            if next_x != x or next_y != y:
                next_spaces.append(((next_x, next_y), next_dist))
        return next_spaces
    def isSpace(self, maze, x, y):
        m, n = len(maze), len(maze[0])
        return 0 <= x < m and 0 <= y < n and maze[x][y] == 0
class IndexPriorityQueue(object):
    def __init__(self):
        self.data = []
        self.key_index = {}
    def size(self):
        return len(self.data)
    def contains(self, key):
        return key in self.key_index
    def getDistance(self, key):
        return self.data[self.key_index[key]][1]
    def push(self, key, val):
        self.data.append((key, val))
        index = self.size() - 1
        self.key_index[key] = index
        self.shiftUp(index)
    def pop(self):
        self.swap(0, self.size() - 1)
        key, val = self.data.pop()
        del self.key_index[key]
        self.shiftDown(0)
        return key, val
    def change(self, key, val):
        index = self.key_index[key]
        self.data[index][1] = val
        self.shiftUp(index)
        self.shiftDown(index)
    def shiftUp(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if not self.less(index, parent):
                break
            self.swap(index, parent)
            index = parent
    def shiftDown(self, index):
        while index * 2 + 1 < self.size():
            left_child = index * 2 + 1
            right_child = left_child + 1
            min_child = left_child
            if right_child < self.size() and self.less(right_child, left_child):
                min_child = right_child
            if not self.less(min_child, index):
                break
            self.swap(min_child, index)
            index = min_child
    def less(self, index1, index2):
        return self.data[index1][1] < self.data[index2][1]
    def swap(self, index1, index2):
        self.data[index1], self.data[index2] = self.data[index2], self.data[index1]
        self.key_index[self.data[index1][0]] = index1
        self.key_index[self.data[index2][0]] = index2
#主函数
if __name__ == '__main__':
    maze = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]]
    start = [0, 4]
    destination = [4, 4]
    print("迷宫是：", maze)
    print("初始地点是:", start)
    print("终点是：", destination)
    solution = Solution()
    print("最少的步数是:", solution.shortestDistance(maze, start, destination))