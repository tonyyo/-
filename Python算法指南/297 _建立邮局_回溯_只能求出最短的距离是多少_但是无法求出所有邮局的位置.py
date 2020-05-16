import collections
from collections import deque
import sys


class Solution:
    def shortestDistance1(self, grid):
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        dist = [[sys.maxsize for j in range(n)] for i in range(m)]
        reachable_count = [[0 for j in range(n)] for i in range(m)]
        min_dist = sys.maxsize
        buildings = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.bfs(grid, i, j, dist, m, n, reachable_count)
                    buildings += 1
        for i in range(m):
            for j in range(n):
                if reachable_count[i][j] == buildings and dist[i][j] < min_dist:
                    min_dist = dist[i][j]
        return min_dist if min_dist != sys.maxsize else -1

    def bfs(self, grid, i, j, dist, m, n, reachable_count):
        visited = [[False for y in range(n)] for x in range(m)]
        visited[i][j] = True
        q = deque([(i, j, 0)])
        while q:
            i, j, l = q.popleft()
            if dist[i][j] == sys.maxsize:
                dist[i][j] = 0
            dist[i][j] += l
            for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = i + x, j + y
                if -1 < nx < m and -1 < ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    if grid[nx][ny] == 0:
                        q.append((nx, ny, l + 1))
                        reachable_count[nx][ny] += 1

    def shortestDistance(self, grid):
        rowNum = len(grid)
        colNum = len(grid[0])
        sum = [[0] * colNum for _ in range(rowNum)]
        for i in range(rowNum):
            for j in range(colNum):
                if grid[i][j] == 1:
                    visited = [[0] * colNum for _ in range(rowNum)]
                    self.dfs(grid, visited, sum, i, j)
        return sum

    def dfs(self, grid, visited, sum, i, j):
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        queue = deque()
        queue.append((i, j))
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nextX = x + dx[i]
                nextY = y + dy[i]
                if not (0 <= nextX < len(grid) and 0 <= nextY < len(grid[0])) or visited[nextX][nextY] != 0 or \
                        grid[nextX][nextY] == 2:
                    continue
                queue.append((nextX, nextY))
                visited[nextX][nextY] = visited[x][y] + 1
                sum[nextX][nextY] += visited[nextX][nextY]

                # 主函数


if __name__ == '__main__':
    grid = [[0, 1, 0, 0, 0], [1, 0, 0, 2, 1], [0, 1, 0, 0, 0]]
    print("网格是：", grid)
    solution = Solution()
    print("最近的距离是：", solution.shortestDistance(grid))
