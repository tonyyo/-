import sys

class Solution:
    def minCut(self, s: str) -> int:
        N = len(s)
        if N == 0 or N == 1:
            return 0
        dp = [sys.maxsize] * N  # dp[i]表示以s[i]结尾的最小分割次数
        dp[0] = 0
        for i in range(N):
            for j in range(i):
                if self.isHuiwen(s[:i+1]): # 特俗情况
                    dp[i] = 0
                    break
                elif self.isHuiwen(s[j + 1: i + 1]):
                    dp[i] = min(dp[i], dp[j] + 1)
        return dp[-1]

    def isHuiwen(self, s):
        return s[::-1] == s

if __name__ == '__main__':
    solution = Solution()
    print(solution.minCut("aab"))