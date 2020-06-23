class Solution:
    def rob(self, nums: [int]) -> int:
        N = len(nums)
        # dp = [0] * (N + 1)  # dp[i] 表示打劫前n家商店的最高金额
        if N == 0:
            return 0
        if N == 1:
            return nums[0]
        pre, cur = 0, nums[0]  # pre表示往前两个数，cur表示往前一个数
        for i in range(2, N + 1):
            pre, cur = cur, max(cur, pre + nums[i - 1])
        return cur

if __name__ == '__main__':
    solution = Solution()
    nums = [1,2,3,1]
    print(solution.rob(nums))
