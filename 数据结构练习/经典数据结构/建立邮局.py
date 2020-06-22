import collections
import copy
import sys


class Solution:
    def shortestDistance(self, grid):
        if len(grid) == 0:
            return 0
        M, N = len(grid), len(grid[0])
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        template = [[0] * N for _ in range(M)]
        sum = [[0] * N for _ in range(M)]
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 2:
                    template[i][j] = -1
                else:
                    template[i][j] = sys.maxsize
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    minDistanceArr = copy.deepcopy(template)
                    minDistanceArr[i][j] = 0
                    queue = collections.deque()
                    queue.append((i, j))
                    while queue:
                        x, y = queue.popleft()
                        for k in range(4):
                            nextX, nextY = x + dx[k], y + dy[k]
                            if not (0 <= nextX < M and 0 <= nextY < N) or minDistanceArr[nextX][nextY] <= minDistanceArr[x][y] + 1:
                                continue
                            if (nextX, nextY) not in queue:
                                queue.append((nextX, nextY))
                            minDistanceArr[nextX][nextY] = minDistanceArr[x][y] + 1
                            sum[nextX][nextY] += minDistanceArr[nextX][nextY]
        return sum
if __name__ == '__main__':
    grid = [[0, 1, 0, 0, 0],
            [1, 0, 0, 2, 1],
            [0, 1, 0, 0, 0]]
    print("网格是：", grid)
    solution = Solution()
    print("最近的距离是：", solution.shortestDistance(grid))
