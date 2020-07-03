import sys
class Solution:
    def maxSubArray(self, nums):
        N, maxSum = len(nums), -sys.maxsize
        # dp = [-sys.maxsize] * N
        # dp[0] = nums[0]
        # maxSum = max(dp[0], maxSum) # 位置0也要比较
        pre = nums[0]
        maxSum = max(pre, maxSum)
        for i in range(1, N):
            # dp[i] = max(dp[i - 1] + nums[i], nums[i])
            # maxSum = max(maxSum, dp[i])
            pre = max(pre + nums[i], nums[i])
            maxSum = max(maxSum, pre)
        return maxSum

if __name__ == '__main__':
    temp = Solution()
    nums2 = [4,2,1,4,-1,2,7,4,-3]
    print ("输出："+str(temp.maxSubArray(nums2)))

# import sys
# class Solution:
#     def maxSubArray(self, nums):
#         min_sum, max_sum = 0, -sys.maxsize
#         prefix_sum = 0
#         for num in nums:
#             prefix_sum += num  # 求出前n项和
#             min_sum = min(min_sum, prefix_sum) #找到最小和数组
#             max_sum = max(max_sum, prefix_sum - min_sum)  # 前n项和减去上次找到的最小和数组等于目前最大和子数组
#         return max_sum