class Solution:
    def maxCoins1(self, nums):
        if not nums:
            return 0
        nums = [1, *nums, 1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 2, n):
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j])
        return dp[0][n - 1]

    def maxCoins(self, nums):
        sum = 0
        while len(nums) != 0:
            if len(nums) >= 3:
                min_num = min(nums[1 : len(nums) - 1])
            else:
                min_num = min(nums)
            i = nums.index(min_num)
            if len(nums) == 1:
                sum += nums[i]
            elif i == 0:
                sum += nums[i] * nums[i + 1]
            elif i == len(nums) - 1:
                sum += nums[i - 1] * nums[i]
            else:
                sum += nums[i - 1] * nums[i] * nums[i + 1]
            nums.remove(min_num)
        return sum

# 主函数
if __name__ == '__main__':
    nums = [4, 1, 5, 10]
    print("初始数组：", nums)
    solution = Solution()
    print("最多分数：", solution.maxCoins(nums))
