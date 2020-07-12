import sys


class Solution:
    def maxProduct(self, nums):
        N, maxProduct = len(nums), -sys.maxsize
        if N == 1:
            return nums[0]
        # positive = [-sys.maxsize] * N
        # negative = [sys.maxsize] * N
        pos, neg = 0, 0
        for i in range(N):
            if i == 0:
                # positive[0], negative[0] = nums[0], nums[0]
                pos, neg = nums[0], nums[0]
            else:
                if nums[i] < 0:  # 小于0时乘以最小值反而是最大值，所以要调换顺序
                    # positive[i-1], negative[i-1] = negative[i-1], positive[i-1]
                    pos, neg = neg, pos
                # positive[i] = max(positive[i-1] * nums[i], nums[i])
                # negative[i] = min(negative[i-1] * nums[i], nums[i])
                pos = max(pos * nums[i], nums[i])
                neg = min(neg * nums[i], nums[i])
            # maxProduct = max(maxProduct, positive[i])
            maxProduct = max(maxProduct, pos)
        return maxProduct

    def maxProduct2(self, nums: [int]) -> int:
        maxProduct = -2e32

        N = len(nums)
        # dp = [0] * N  # dp[i] 表示以第i个元素结尾的连续最大乘积
        imin = 0   # 第i个元素结尾的连续最小乘积， 一定是负数
        imax = 0   # 第i个元素结尾的连续最大成绩， 一定是正数
        for i in range(N):
            if i == 0:
                imin = nums[i]
                imax = nums[i]
            else:
                if nums[i] < 0:
                    imin, imax = imax, imin
                imin = min(imin * nums[i], nums[i])
                imax = max(imax * nums[i], nums[i])
            maxProduct = max(maxProduct, imax)
        return maxProduct

if __name__ == '__main__':
    solution = Solution()
    nums = [3,-1,4]
    print(solution.maxProduct(nums))