class Solution:
    def pacificAtlantic(self, matrix: [[int]]) -> [[int]]:
        if len(matrix) == 0:
            return []
        M, N = len(matrix), len(matrix[0])
        visit1 = [[0] * N for _ in range(M)]
        visit2 = [[0] * N for _ in range(M)]
        res = []

        for i in range(M):
            self.dfs(matrix, i, 0, visit1)
            self.dfs(matrix, i, N - 1, visit2)
        for j in range(N):
            self.dfs(matrix, 0, j, visit1)
            self.dfs(matrix, M - 1, j, visit2)
        for i in range(M):
            for j in range(N):
                if visit1[i][j] == 1 and visit2[i][j] == 1:
                    res.append([i, j])
        return res


    def dfs(self, matrix, x, y, visit):
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        M, N = len(matrix),len(matrix[0])
        import collections
        queue = collections.deque()
        queue.append((x, y))
        while queue:
            x, y = queue.popleft()
            visit[x][y] = 1
            for i in range(4):
                nextX, nextY = x + dx[i], y + dy[i]
                if not (0 <= nextX < M and 0 <= nextY < N) or visit[nextX][nextY] == 1 or matrix[nextX][nextY] < matrix[x][y]:
                    continue
                queue.append((nextX,nextY))
