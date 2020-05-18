def inbound(x, y, n, m):
    return 0 <= x < n and 0 <= y < m


class Solution:
    def pacificAtlantic1(self, matrix):
        if not matrix or not matrix[0]:
            return []
        n, m = len(matrix), len(matrix[0])
        p_visited = [[False] * m for _ in range(n)]
        a_visited = [[False] * m for _ in range(n)]
        for i in range(n):
            self.dfs1(matrix, i, 0, p_visited)
            self.dfs1(matrix, i, m - 1, a_visited)
        for j in range(m):
            self.dfs1(matrix, 0, j, p_visited)
            self.dfs1(matrix, n - 1, j, a_visited)
        res = []
        for i in range(n):
            for j in range(m):
                if p_visited[i][j] and a_visited[i][j]:
                    res.append([i, j])
        return res

    def dfs1(self, matrix, x, y, visited):
            visited[x][y] = True
            dx = [0, 1, 0, -1]
            dy = [1, 0, -1, 0]
            for i in range(4):
                n_x = dx[i] + x
                n_y = dy[i] + y
                if not inbound(n_x, n_y, len(matrix), len(matrix[0])) or visited[n_x][n_y] or matrix[n_x][n_y] < \
                        matrix[x][
                            y]:
                    continue  # 回溯中 continue比return好用
                self.dfs1(matrix, n_x, n_y, visited)

    def pacificAtlantic(self, matrix):
        rowNum = len(matrix)
        colNum = len(matrix[0])
        res = []
        self.dx = [0, 1, 0, -1]
        self.dy = [1, 0, -1, 0]
        p = [[False] * colNum for _ in range(rowNum)]
        a = [[False] * colNum for _ in range(rowNum)]
        for i in range(rowNum):
            self.dfs(matrix, i, 0, p)
            self.dfs(matrix, i, colNum - 1, a)
        for j in range(colNum):
            self.dfs(matrix, 0, j, p)
            self.dfs(matrix, rowNum - 1, j, a)
        for i in range(rowNum):
            for j in range(colNum):
                if a[i][j] and p[i][j]:
                    res.append([i, j])
        return res

    def dfs(self, matrix, x, y, visited):
        visited[x][y] = True
        for i in range(4):
            nextX = x + self.dx[i]
            nextY = y + self.dy[i]
            if not inbound(nextX, nextY, len(matrix), len(matrix[0])) or matrix[nextX][nextY] < matrix[x][y] or visited[nextX][nextY]:
                continue
            self.dfs(matrix, nextX, nextY, visited)



# 主函数
if __name__ == '__main__':
    matrix = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
    solution = Solution()
    print("给定矩阵是：", matrix)
    print("满足条件的点坐标是：", solution.pacificAtlantic(matrix))
