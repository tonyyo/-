class Solution:
    flag = False
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    def hasPath(self, strings, rows, cols, path):
        matrix = [["0"] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                matrix[i][j] = strings[i * cols + j]
        print matrix

        for i in range(rows):
            for j in range(cols):
                visit = [["0"] * cols for _ in range(rows)]
                if matrix[i][j] == path[0]:
                    pos = [i, j]
                    visit[i][j] = "-1"
                    self.dfs(matrix, pos, visit, 0, path)
                    if self.flag == True:
                        return True
        return False

    def dfs(self, matrix, pos, visit, start, path):
        if start == len(path) - 1 and matrix[pos[0]][pos[1]] == path[start]:
            self.flag = True
            return
        x, y = pos[0], pos[1]
        for i in range(4):
            nextX, nextY = x + self.dx[i], y+ self.dy[i]
            if not self.inbound(nextX, nextY, matrix) or visit[nextX][nextY] == "-1" or matrix[nextX][nextY] != path[start + 1]:
                continue
            else:
                visit[nextX][nextY] = "-1"
                self.dfs(matrix, [nextX, nextY], visit, start + 1, path)
                visit[nextX][nextY] = "0"

    def inbound(self, x, y, matrix):
        return 0 <= x < len(matrix) and 0 <= y < len(matrix[0])

if __name__ == '__main__':
    solution = Solution()
    strings = "ABCESFCSADEE"
    print(solution.hasPath(strings, 3, 4, "ABCCED"))