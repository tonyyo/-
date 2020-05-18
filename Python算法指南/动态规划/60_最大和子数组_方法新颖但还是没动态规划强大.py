class Solution:
    def maxSubArray(self, nums):
        dp = [0 for i in range(len(nums) + 1)] # 前i个元素的子数组最大和
        sum = [0 for i in range(len(nums) + 1)] # 前i个元素的和
        for i in range(1, len(dp)):
            sum[i] = sum[i - 1] + nums[i - 1]
            if sum[i] < nums[i - 1]:
                dp[i] = nums[i - 1]
            else:
                dp[i] = max(dp[i - 1], sum[i - 1] + nums[i - 1])
        print(dp)
        return dp[len(dp) - 1]

if __name__ == '__main__':
    temp = Solution()
    nums2 = [4, 2, 1, 4, -1, 2, 7, 4, -3]
    print("输出：" + str(temp.maxSubArray(nums2)))
