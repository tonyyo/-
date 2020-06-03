class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        maxSum = -2e32
        N = len(nums)
        #dp = [0] * N  # dp[i]表示以nums[i]结尾的最大连续子数组和
        pre = 0  # 空间优化，只需要保持前一个
        for i in range(N):
            if i == 0:
                pre = nums[0]
            else:
                pre = max(pre + nums[i], nums[i])
            maxSum = max(maxSum, pre)
        return maxSum
if __name__ == '__main__':
    solution = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(solution.maxSubArray(nums))