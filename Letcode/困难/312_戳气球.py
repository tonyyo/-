class Solution:
    def maxCoins(self, nums: [int]) -> int:
        N = len(nums)
        dp = [[0] * N for _ in range(N)]  # dp[i][j]表示从第i个位置到第j个位置获得的最大硬币数
        dp[0][0] = nums[0] + nums[1]
        for i in range(N - 3, -1, -1):  # 因为最终返回的结果是dp[0][N - 1],所以从后往前计算
            for j in range(i + 2, N):
                for k in range(i, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k+1][j] + nums[i] * nums[k] * nums[j])
        return dp[0][N - 1]


