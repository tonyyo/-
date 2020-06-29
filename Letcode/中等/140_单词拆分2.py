class Solution:
    def wordBreak(self, s: str, wordDict: [str]) -> bool:
        N = len(s)
        dp = [[] for _ in range(N + 1)]
        dp[0].append("1")
        for i in range(N + 1):
            list = []    # 存多个句子
            for j in range(i + 1):
                cur = s[j : i]
                if len(dp[j]) != 0 and cur in wordDict:
                    for x in dp[j]:
                        midSymbol = "" if len(x) == 0 else " "
                        list.append(x + midSymbol + cur)
            dp[i] = list if len(list) != 0 else dp[i]
        # print(dp)
        result = []
        for x in dp[-1]:
            result.append(x[2:])
        return result
if __name__ == '__main__':
    s = "leetcode"
    wordDict = ['leet', 'code']
    solution = Solution()
    print(solution.wordBreak(s, wordDict))