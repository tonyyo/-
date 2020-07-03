import sys


class Solution:
    def minSubArray(self, nums):
        N, minSum = len(nums), sys.maxsize
        dp = [sys.maxsize] * N  # dp[i]以nums[i]结尾的最小子数组和
        # dp[0] = nums[0]
        preSum = nums[0]
        for i in range(1, N):
            # dp[i] = min(dp[i - 1] + nums[i], nums[i])
            preSum = min(preSum + nums[i], nums[i])
            minSum = min(minSum, preSum)
        return minSum

if __name__ == '__main__':
    temp = Solution()
    List1 = [1, -1, -2, 1]
    List2 = [3, -2, 2, 1]
    print("输入：" + str(List1))
    print(("输出：" + str(temp.minSubArray(List1))))
    print("输入：" + str(List2))
    print(("输出：" + str(temp.minSubArray(List2))))
