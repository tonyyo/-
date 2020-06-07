class Solution:
    def maxProduct(self, nums: [int]) -> int:
        maxProduct = -2e32

        N = len(nums)
        # dp = [0] * N  # dp[i] 表示以第i个元素结尾的连续最大乘积
        imin = 0   # 第i个元素结尾的连续最小乘积， 一定是负数
        imax = 0   # 第i个元素结尾的连续最大成绩， 一定是正数
        for i in range(N):
            if i == 0:
                imin = nums[i]
                imax = nums[i]
            else:
                if nums[i] < 0:
                    imin, imax = imax, imin
                imin = min(imin * nums[i], nums[i])
                imax = max(imax * nums[i], nums[i])
            maxProduct = max(maxProduct, imax)
        return maxProduct