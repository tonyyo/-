class Solution:
    def rob(self, nums: [int]) -> int:
        N = len(nums)
        return max(self.subRob(nums, 0, N - 2), self.subRob(nums, 1, N - 1))

    def subRob(self, nums, start, end): #从start 偷到 end处能获得的最高金额
        N = len(nums)
        pre, cur = 0, 0
        if N == 1:
            return nums[0]
        else:
            for i in range(start, end + 1):
                pre, cur =cur, max(cur, pre + nums[i])
        return cur


if __name__ == '__main__':
    solution = Solution()
    nums = [1]
    print(solution.rob(nums))