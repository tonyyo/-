import sys


class Solution:
    def minCut(self, s: str) -> int:
        N = len(s)
        if N == 0 or N == 1:
            return 0
        dp = [sys.maxsize] * (N + 1)  # dp[i]表示s的前i个字符串分割回文的最小数
        dp[0], dp[1] = -1, 0     # -1 是因为放置最前面是空而再切一刀的情况
        for i in range(N + 1):
            for j in range(i):  # i 领先于数组索引，所以这里是正好的，不需要i + 1
                if self.isHuiwen(s[j : i]):
                    dp[i] = min(dp[i], dp[j] + 1)
        return dp[-1]

    def isHuiwen(self, s):
        return s[::-1] == s

if __name__ == '__main__':
    solution = Solution()
    print(solution.minCut("aab"))