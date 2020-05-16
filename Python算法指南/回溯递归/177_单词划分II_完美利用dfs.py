class Solution:
    def wordBreak(self, s, wordDict):
        List = []
        self.dfs(s, wordDict, "", List)
        return List

    def dfs(self, s, wordDict, string, List):
        if len(s) == 0:
            List.append(string)
        for i in range(1, len(s) + 1): # 要取到空的话，i必须要等于len
            if s[:i] not in wordDict:
                continue
            else:
                self.dfs(s[i:], wordDict, string + " " + s[:i], List)


# 主函数
if __name__ == '__main__':
    s = "expressions"
    wordDict = ["express", "ex", "press", "demo", "ions"]
    print("String 是:", s)
    print("dict是:", wordDict)
    solution = Solution()
    print("结果是：", solution.wordBreak(s, wordDict))
