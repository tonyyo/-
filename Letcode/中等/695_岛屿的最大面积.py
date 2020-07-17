class Solution:
    def maxAreaOfIsland(self, grid: [[int]]) -> int:
        dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
        import collections
        queue = collections.deque()
        M, N, maxArea = len(grid), len(grid[0]), 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    area = 0
                    queue.append([i, j]) # 先要进队列
                    while queue:
                        x, y = queue.popleft() # 循环后出队列
                        grid[x][y] = 0  # 置0
                        area += 1   # 真正访问的位置
                        for k in range(4):
                            nextX, nextY = x + dx[k], y + dy[k]
                            if not (0 <= nextX < M and 0 <= nextY < N) or grid[nextX][nextY] == 0:
                                continue
                            if (nextX, nextY) not in queue: # 不能存在queue中
                                queue.append((nextX, nextY))
                    maxArea = max(maxArea, area)
        return maxArea


