class Solution:
    def wordBreak(self, s: str, wordDict: [str]):
        N = len(s)
        if N == 0:
            return []
        dp = [[] for _ in range(N + 1)]
        dp[0] = [""]
        for i in range(1, N + 1):
            list = []    # 存多个句子
            for j in range(i):
                cur = s[j : i]
                if cur in wordDict:
                    for x in dp[j]:
                        midSymbol = "" if len(x) == 0 else " "
                        list.append(x + midSymbol + cur)
            dp[i] = list
        return dp[-1]
if __name__ == '__main__':
    s = "leetcode"
    wordDict = ['leet', 'code']
    solution = Solution()
    print(solution.wordBreak(s, wordDict))