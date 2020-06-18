import collections


class Solution:
    def wallsAndGates2(self, rooms):
        if len(rooms) == 0 or len(rooms[0]) == 0:
            return rooms
        m = len(rooms)
        n = len(rooms[0])
        import queue
        queue = queue.Queue()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.put((i, j))
        while not queue.empty():
            x, y = queue.get()
            for dx, dy in directions:
                new_x = x + dx
                new_y = y + dy
                if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n or rooms[new_x][new_y] < rooms[x][y] + 1:
                    continue
                rooms[new_x][new_y] = rooms[x][y] + 1
                queue.put((new_x, new_y))
        return rooms

    def wallsAndGates(self, rooms):
        rowNum = len(rooms)
        colNum = len(rooms[0])
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        import collections
        duilie = collections.deque()
        for i in range(rowNum):
            for j in range(colNum):
                if rooms[i][j] == 0:
                    duilie.append([i, j])
        while duilie:
            x, y = duilie.popleft()
            for i in range(4):
                nextX = x + dx[i]
                nextY = y + dy[i]
                if nextX < 0 or nextY < 0 or nextX >= rowNum or nextY >= colNum or rooms[nextX][nextY] < rooms[x][y] + 1:
                    continue
                rooms[nextX][nextY] = rooms[x][y] + 1
                duilie.append([nextX, nextY])
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
