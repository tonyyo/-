class Solution:
    def wordBreak(self, s, wordDict):
        List = []
        self.dfs2(s, wordDict, "", List)
        return List

    def dfs2(self, s, wordDict, string, List):
        if len(s) == 0:
            List.append(string.strip())
            return
        for i in range(1, len(s) + 1):
            prefix = s[:i]
            if prefix not in wordDict:
                continue
            self.dfs2(s[i:], wordDict, string + " " + prefix, List)

# 主函数
if __name__ == '__main__':
    s = "expressions"
    wordDict = set(["express", "ex", "press", "demo", "ions"])
    print("String 是:", s)
    print("dict是:", wordDict)
    solution = Solution()
    print("结果是：", solution.wordBreak(s, wordDict))
