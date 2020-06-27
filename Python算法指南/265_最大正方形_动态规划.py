class Solution:
    def maximalSquare(self, matrix):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        rowNum = len(matrix)
        colNum = len(matrix[0])
        MAX = 0
        for i in range(rowNum):
            for j in range(colNum):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        matrix[i][j] = 1
                    else:
                        matrix[i][j] = min(matrix[i - 1][j], matrix[i - 1][j - 1], matrix[i][j - 1]) + 1
                    MAX = max(MAX, matrix[i][j])
        return MAX * MAX
#主函数
if __name__ == '__main__':
    s = [[1, 0, 1, 0, 0], [1, 0, 1, 1, 1], [1, 1, 1, 1, 1], [1, 0, 0, 1, 0]]
    print("初始矩阵：")
    for i in range(0, len(s)):
        print(s[i])
    solution = Solution()
    print("结果：", solution.maximalSquare(s))