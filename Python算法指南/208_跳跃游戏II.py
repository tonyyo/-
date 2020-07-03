import sys


class Solution:
    def jump(self, nums: [int]) -> int:
        n = len(nums)
        maxPos, end, step = 0, 0, 0 # end记录最晚起跳的位置
        for i in range(n - 1):  # 到了倒数第2个位置，无论如何都是要起跳的，肯定能到最后一个位置，到n的话会多跳一步
            if maxPos >= i:  # 能跳到该位置
                maxPos = max(maxPos, i + nums[i])
                if i == end:  # 到了最晚起跳的位置，该起跳了
                    end = maxPos
                    step += 1
        return step

    def jump2(self, nums: [int]) -> int:
        N = len(nums)
        if N == 0:
            return 0
        if N == 1:  # 本身就在最后一个位置，不需要跳
            return 0
        dp = [sys.maxsize] * N
        dp[0], dp[1] = 0, 1
        for i in range(2, N):
            for j in range(i): # 遍历上一步可能的位置
                if nums[j] >= i - j:  # 从该位置能跳到第i个位置
                    dp[i] = min(dp[i], dp[j] + 1)
        return dp[-1]


if __name__ == '__main__':
    temp = Solution()
    List2 = [1, 3, 5, 2, 1, 3, 1, 1]
    steps, result, start = 0, [], 0
    print(("输入：" + str(str(List2))))
    print(temp.jump(List2))
