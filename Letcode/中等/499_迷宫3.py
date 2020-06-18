class Solution:
    def wallsAndGates(self, rooms):
        if len(rooms) == 0:
            return []
        M, N = len(rooms), len(rooms[0])
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        import collections
        queue = collections.deque()
        for i in range(M):
            for j in range(N):
                if rooms[i][j] == 0:
                    queue.append((i, j))
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nextX, nextY = x + dx[i], y + dy[i]
                if not (0 <= nextX < M and 0 <= nextY < N) or rooms[nextX][nextY] == -1 or rooms[nextX][nextY] <= rooms[x][y] + 1:
                    continue
                queue.append((nextX, nextY))
                rooms[nextX][nextY] = rooms[x][y] + 1
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
