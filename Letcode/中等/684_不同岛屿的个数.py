import collections
class Solution:
    def numberofDistinctIslands(self, grid):
        if len(grid) == 0:
            return 0
        M, N = len(grid), len(grid[0])
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        res = []
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    queue = collections.deque()
                    queue.append((i, j))
                    while queue:
                        x, y = queue.popleft()
                        grid[x][y] = 0
                        for k in range(4):
                            nextX, nextY = x + dx[k], y + dy[k]
                            if not (0 <= nextX < M and 0 <= nextY < N) or grid[nextX][nextY] == 0:
                                continue
                            if (nextX, nextY) not in queue:
                                queue.append((nextX, nextY))
                        if not queue:
                            path = (x - i, y - j)
                if path not in res:
                    res.append(path)
        print(grid)
        return res

if __name__ == '__main__':
    grid = [
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1],
        [0, 0, 0, 1, 1]
    ]
    print("矩阵是：", grid)
    solution = Solution()
    print("不同岛屿个数是：", solution.numberofDistinctIslands(grid))
