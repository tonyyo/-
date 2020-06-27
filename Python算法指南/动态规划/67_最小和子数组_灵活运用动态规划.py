import sys


class Solution:
    def minSubArray(self, nums):
        sum, N = sys.maxsize, len(nums)
        # dp = [0] * N  # dp[i]表示已nums[i]结尾的最小和子数组
        # dp[0] = nums[0]
        pre = 0
        for i in range(1, N):
            # dp[i] = min(dp[i - 1] + nums[i], nums[i])
            pre = min(pre + nums[i], nums[i])
            sum = min(sum, pre)
        return sum

if __name__ == '__main__':
    temp = Solution()
    List1 = [1, -1, -2, 1]
    List2 = [3, -2, 2, 1]
    print("输入：" + str(List1))
    print(("输出：" + str(temp.minSubArray(List1))))
    print("输入：" + str(List2))
    print(("输出：" + str(temp.minSubArray(List2))))
