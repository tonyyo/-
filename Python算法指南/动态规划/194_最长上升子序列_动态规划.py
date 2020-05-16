class Solution:
    def longestIncreasingSubsequence(self, nums):
        if nums is None or not nums:
            return 0
        dp = [1] * len(nums) # 前i个元素的最大上升子序列长度
        size = len(nums)
        for i in range(size):
            for j in range(i): # 跟i之前的各个位置交流
                if nums[i] > nums[j]: # 跟第i个位置进行比较，如果大于，那么递增序列家族多了一位，所以加1
                    dp[i] = max(dp[i], dp[j] + 1)
        return dp[-1]

if __name__ == '__main__':
    temp = Solution()
    List2 = [4,2,4,5,3,7]
    print(("输入："+str(List2)))
    print(("输出："+str(temp.longestIncreasingSubsequence(List2))))