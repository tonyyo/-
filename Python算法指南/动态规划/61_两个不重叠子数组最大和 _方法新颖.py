import sys


class Solution:
    def maxTwoSubArrays(self, nums):
        size = len(nums)
        MAX = 0
        for i in range(1, size):
            temp1 = nums[0 : i]
            temp2 = nums[i : ]
            MAX = max(self.maxSubArrays(temp1) + self.maxSubArrays(temp2), MAX)
        return MAX

    def maxSubArrays(self, arr):
        sum, N = -sys.maxsize, len(arr)
        dp = [0] * N
        for i in range(N):
            dp[i] = max(dp[i - 1] + arr[i], arr[i])
            sum = max(sum, dp[i])
        return sum


if __name__ == '__main__':
    temp = Solution()
    nums1 = [0,6,5,2,2,5,1,9,4]
    print(("输入：" + str(nums1)))
    print(("输出：" + str(temp.maxTwoSubArrays(nums1))))
