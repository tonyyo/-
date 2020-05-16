class Solution:
    def longestIncreasingSubsequence(self, nums):
        if nums is None or not nums:
            return 0
        dp = [1] * len(nums)
        for curr, val in enumerate(nums):
            for prev in range(curr):
                if nums[prev] < val:
                    dp[curr] = max(dp[curr], dp[prev] + 1) #https://www.jianshu.com/p/1d429d990224
            print(dp)

        return max(dp)


if __name__ == '__main__':
    temp = Solution()
    List2 = [4,2,4,5,3,7]
    print(("输入："+str(List2)))
    print(("输出："+str(temp.longestIncreasingSubsequence(List2))))