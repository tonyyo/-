class Solution:
    def maximalSquare(self, matrix):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        rowNum, colNum, MAX = len(matrix), len(matrix[0]), 0
        for i in range(rowNum):
            for j in range(colNum):
                matrix[i][j] = int(matrix[i][j])
                if matrix[i][j] == 1:
                    if not (i == 0 or j == 0):
                        matrix[i][j] = min(matrix[i - 1][j], matrix[i - 1][j - 1], matrix[i][j - 1]) + 1
                    MAX = max(MAX, matrix[i][j])  # 第一行第一列自带base case
        return MAX * MAX
#主函数
if __name__ == '__main__':
    s = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    print("初始矩阵：")
    for i in range(0, len(s)):
        print(s[i])
    solution = Solution()
    print("结果：", solution.maximalSquare(s))