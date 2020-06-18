class Solution:
    def islandPerimeter(self, grid: [[int]]) -> int:
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        if len(grid) == 0:
            return 0
        M, N = len(grid), len(grid[0])
        visit = [[0] * N for _ in range(M)]
        Perim = 0
        import collections
        queue = collections.deque()
        flag = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    queue.append((i, j))
                    flag = 1
                    break
            if flag == 1:
                break
        while queue:
            x, y = queue.popleft()
            visit[x][y] = 2
            Perim += 4
            for i in range(4):
                nextX, nextY = x + dx[i], y + dy[i]
                if not (0 <= nextX < M and 0 <= nextY < N) or visit[nextX][nextY] == 2 or grid[nextX][nextY] == 0:
                    continue
                if (nextX, nextY) not in queue:  # 特别注意，不要将queue中原本存在的再加一遍。
                    queue.append((nextX, nextY))
                Perim -= 2
        return Perim
if __name__ == '__main__':
    grid =  [[1,1],[1,1]]
    solution = Solution()
    print("初始化的数组", grid)
    print("岛的周长是：", solution.islandPerimeter(grid))
