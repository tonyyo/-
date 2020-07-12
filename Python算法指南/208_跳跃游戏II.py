import sys


class Solution:
    class Solution:
        def jump(self, nums: [int]) -> int:
            N = len(nums)
            if N == 1:
                return 0
            maxPos, end, step = nums[0], nums[0], 1
            for i in range(1, N - 1): # 跳到最后第二个就好
                if maxPos >= i:
                    maxPos = max(maxPos, i + nums[i])
                    if i == end:
                        step += 1
                        end = maxPos
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
