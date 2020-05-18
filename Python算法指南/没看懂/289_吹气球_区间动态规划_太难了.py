class Solution:
    def maxCoins1(self, nums):
        if not nums:
            return 0
        nums = [1, *nums, 1] # 在数组nums两边补1
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):  # 左指针
            for j in range(i + 2, n): # 右指针
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j])
        print(dp)
        return dp[0][n - 1]

# 主函数
if __name__ == '__main__':
    nums = [4, 1, 5, 10]
    print("初始数组：", nums)
    solution = Solution()
    print("最多分数：", solution.maxCoins1(nums))
