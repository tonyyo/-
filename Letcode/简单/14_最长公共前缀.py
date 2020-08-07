class Solution:
    def longestCommonPrefix(self, strs: [str]) -> str:
        maxPrefix = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(maxPrefix) != 0: # 直到找到公共前缀
                maxPrefix = maxPrefix[:-1] # 去掉最后一个元素后，仍然是公共前缀
        return maxPrefix
