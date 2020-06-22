import collections
from collections import deque
import sys


class Solution:
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
