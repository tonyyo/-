def inbound(x, y, n, m):
    return 0 <= x < n and 0 <= y < m


class Solution:
    def pacificAtlantic(self, matrix):
        rowNum, colNum = len(matrix), len(matrix[0])
        result = []
        Pacific = [[0 for _ in range(colNum)] for _ in range(rowNum)]
        Atlantic = [[0 for _ in range(colNum)] for _ in range(rowNum)]
        for i in range(rowNum):
            Pacific[i][0] = 1  # Pacific第一列初始化
            Atlantic[i][colNum - 1] = 1  # Atlantic最后一列初始化
            self.dfs(matrix, i, 0, Pacific)
            self.dfs(matrix, i, colNum - 1, Atlantic)
        for j in range(colNum):
            Pacific[0][j] = 1  # Pacific第一行初始化
            Atlantic[rowNum - 1][j] = 1  # Atlantic最后一行初始化
            self.dfs(matrix, 0, j, Pacific)
            self.dfs(matrix, rowNum - 1, j, Atlantic)
        for i in range(rowNum):
            for j in range(colNum):
                if Pacific[i][j] == Atlantic[i][j]:
                    result.append((i, j))
        return result

    def dfs(self, matrix, x, y, visit): # 这不是回溯，这就是个dfs递归，出口就是可走方向都完了，程序结束就是出口
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        rowNum, colNum = len(matrix), len(matrix[0])
        for i in range(4):
            nextX = x + dx[i]
            nextY = y + dy[i]
            if not (0 <= nextX < rowNum and 0 <= nextY < colNum) or visit[nextX][nextY] == 1 \
                    or matrix[x][y] > matrix[nextX][nextY]:
                continue
            else:
                visit[x][y] = 1
                self.dfs(matrix, nextX, nextY, visit)




if __name__ == '__main__':
    matrix = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
    solution = Solution()
    print("给定矩阵是：", matrix)
    print("满足条件的点坐标是：", solution.pacificAtlantic(matrix))
