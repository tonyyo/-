class Solution:
    def maxSquare(self, matrix):
        rowNum, colNum = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(colNum + 1)] for _ in range(rowNum + 1)]
        for i in range(rowNum):
            for j in range(colNum):
                dp[i][j] = matrix[i][j]     # dp相比matrix首尾各多一行0
        MAX = 0
        for i in range(rowNum):
            for j in range(colNum):
                if dp[i][j] == 1:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1 # 取左、左上、上边长最小值+1
                    MAX = max(MAX, dp[i][j]) # 沿途记录最大边长
        print(dp)
        return MAX * MAX

#主函数
if __name__ == '__main__':
    s = [[1, 0, 1, 0, 0], [1, 0, 1, 1, 1], [1, 1, 1, 1, 1], [1, 0, 0, 1, 0]]
    print("初始矩阵：")
    for i in range(0, len(s)):
        print(s[i])
    solution = Solution()
    print("结果：", solution.maxSquare(s))