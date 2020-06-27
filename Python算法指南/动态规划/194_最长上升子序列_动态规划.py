class Solution:
    def lengthOfLIS(self, nums):
        if nums is None or not nums:
            return 0
        dp = [1] * len(nums) # 以第i个元素结尾的最大上升子序列长度
        MAX, size = 0, len(nums)
        for i in range(size):
            for j in range(i): # 跟i之前的各个位置交流
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            MAX = max(MAX, dp[i])
        return MAX

if __name__ == '__main__':
    temp = Solution()
    List2 = [1,3,6,7,9,4,10,5,6]
    print(("输入："+str(List2)))
    print(("输出："+str(temp.lengthOfLIS(List2))))