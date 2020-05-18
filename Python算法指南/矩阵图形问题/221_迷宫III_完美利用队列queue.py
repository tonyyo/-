import collections
class Solution:
    def wallsAndGates2(self, rooms):
        rowNum = len(rooms)
        colNum = len(rooms[0])
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        import queue
        duilie = queue.Queue()
        for i in range(rowNum):
            for j in range(colNum):
                if rooms[i][j] == 0:
                    duilie.put([i, j])
        while not duilie.empty():
            x, y = duilie.get()
            for i in range(4):
                nextX = x + dx[i]
                nextY = y + dy[i]
                if nextX < 0 or nextY < 0 or nextX >= rowNum or nextY >= colNum or rooms[nextX][nextY] < rooms[x][y] + 1:
                    continue
                rooms[nextX][nextY] = rooms[x][y] + 1
                duilie.put([nextX, nextY])
        return rooms

    def wallsAndGates(self, rooms):
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        rowNum, colNum = len(rooms), len(rooms[0])
        queue = collections.deque()
        for i in range(rowNum):
            for j in range(colNum):
                if rooms[i][j] == 0:
                    queue.append([i, j])  # 把所有为0的项加入queue，因为后续不会加入为0的项了，遍历将会不完整
        while queue:
            [x, y] = queue.popleft()
            for i in range(4):
                nextX, nextY = x + dx[i], y + dy[i]
                # 如果越界或者下一个值小于上一个值加1，就换个方向。
                if not (0 <= nextX < rowNum and 0 <= nextY < colNum) \
                        or rooms[nextX][nextY] < rooms[x][y] + 1:
                    continue
                else:
                    rooms[nextX][nextY] = rooms[x][y] + 1
                    queue.append([nextX, nextY])
        return rooms
# 主函数
if __name__ == '__main__':
    INF = 2147483647
    matrix = [[INF, -1, 0, INF],
              [INF, INF, INF, -1],
              [INF, -1, INF, -1],
              [0, -1, INF, INF]]
    solution = Solution()
    print("运行的结果是：", solution.wallsAndGates(matrix))
