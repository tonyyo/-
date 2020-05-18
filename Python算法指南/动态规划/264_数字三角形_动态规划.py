class Solution:
    def minimumTotal(self, triangle):
        dp = triangle.copy()
        for i in range(1, len(dp)): # 第一行没有上家
            for j in range(len(dp[i])):
                if j == 0:
                    dp[i][j] = dp[i][j] + dp[i - 1][j]
                elif j == len(dp[i]) - 1:
                    dp[i][j] = dp[i][j] + dp[i - 1][j -1]
                else:
                    dp[i][j] = min(dp[i][j] + dp[i - 1][j - 1], dp[i][j] + dp[i - 1][j])
        print(dp)
        return min(dp[len(dp) - 1])
#主函数
if __name__ == '__main__':
    triangle = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]
    print("初始数字三角形：")
    for i in range(0,len(triangle)):
        print(triangle[i])
    solution = Solution()
    print("最小路径：", solution.minimumTotal(triangle))