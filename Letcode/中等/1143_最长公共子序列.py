class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        M, N = len(text1), len(text2)
        dp = [[0] * (N + 1) for _ in range(M + 1)]  # dp[i][j] 表示text1[:i]和text2[:j]的最长公共子序列
        maxLen = 0
        for i in range(M):
            for j in range(N):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                maxLen = max(dp[i][j], maxLen)
        return maxLen
