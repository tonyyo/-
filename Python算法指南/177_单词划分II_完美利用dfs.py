class Solution:
    def wordBreak(self, s, wordDict):
        List = []
        self.dfs2(s, wordDict, "", List)
        return List

    # 找到s的所有切割方案并返回
    # def dfs(self, s, wordDict, memo):
    #     if s in memo:
    #         return memo[s]
    #     if len(s) == 0:
    #         return []
    #     partitions = []
    #     for i in range(1, len(s)):
    #         prefix = s[:i]
    #         if prefix not in wordDict:
    #             continue
    #         sub_partitions = self.dfs(s[i:], wordDict, memo)
    #         for partition in sub_partitions:
    #             partitions.append(prefix + " " + partition)
    #     if s in wordDict:
    #         partitions.append(s)
    #     memo[s] = partitions
    #     print(memo[s])
    #     return partitions

    def dfs2(self, s, wordDict, string, List):
        if len(s) == 0:
            List.append(string.strip())
        for i in range(1, len(s) + 1):
            prefix = s[:i]
            if prefix not in wordDict:
                continue
            self.dfs2(s[i:], wordDict,string + " " + prefix, List)

# 主函数
if __name__ == '__main__':
    s = "expressions"
    wordDict = set(["express", "ex", "press", "demo", "ions"])
    print("String 是:", s)
    print("dict是:", wordDict)
    solution = Solution()
    print("结果是：", solution.wordBreak(s, wordDict))
