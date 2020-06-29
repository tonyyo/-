class Solution:
    def wordBreak(self, s: str, wordDict: [str]) -> bool:
        N = len(s)
        dp = [False] * (N + 1)
        dp[0] = True
        for i in range(N + 1):
            for j in range(i + 1):
                cur = s[j : i]
                if dp[j] and cur in wordDict:
                    dp[i] = True
                    break
        return dp[-1]
if __name__ == '__main__':
    s = "leetcode"
    wordDict = ['leet', 'code']
    solution = Solution()
    print(solution.wordBreak(s, wordDict))