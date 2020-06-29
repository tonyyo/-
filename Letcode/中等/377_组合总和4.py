class Solution:
    def combinationSum4(self, nums: [int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for x in nums:
            if x <= target:  # 放置nums = [9], target = 3的情况出现越界
                dp[x] = 1
        for i in range(target + 1):
            for j in nums:
                dp[i] += dp[i - j]
        return dp[target]
