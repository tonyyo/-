class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        N = len(s)
        dp = [[1] * N for _ in range(N)]
        for i in range(N - 1, -1, -1): # i从后往前，当i = 0时，得到最终结果
            for j in range(i + 1, N):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][N - 1]

if __name__ == '__main__':
    temp = Solution()
    string1 = "abcdedcb"
    string2 = "qwerfdfdfg"
    print(temp.longestPalindromeSubseq(string1))
