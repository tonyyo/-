class Solution:
    def maxSquare1(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        n, m = len(matrix), len(matrix[0])
        #初始化
        f = [[0] * m for _ in range(n)]
        for i in range(m):
            f[0][i] = matrix[0][i]
        edge = max(matrix[0])
        for i in range(1, n):
            f[i][0] = matrix[i][0]
            for j in range(1, m):
                if matrix[i][j]:
                    f[i][j] = min(f[i - 1][j], f[i][j - 1], f[i - 1][j - 1]) + 1
                else:
                    f[i][j] = 0
            edge = max(edge, max(f[i]))
        return edge * edge

    def maxSquare(self, matrix):
        rowNum = len(matrix)
        colNum = len(matrix[0])
        MAX = 0
        for i in range(1, rowNum):
            for j in range(1, colNum):
                if matrix[i][j] == 1:
                    matrix[i][j] = min(matrix[i - 1][j], matrix[i - 1][j - 1], matrix[i][j - 1]) + 1
                    MAX = max(MAX, matrix[i][j])
        return MAX * MAX
#主函数
if __name__ == '__main__':
    s = [[1, 0, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 1, 1, 1], [1, 0, 0, 1, 0]]
    print("初始矩阵：")
    for i in range(0, len(s)):
        print(s[i])
    solution = Solution()
    print("结果：", solution.maxSquare(s))