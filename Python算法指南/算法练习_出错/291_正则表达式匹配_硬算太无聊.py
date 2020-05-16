class Solution:
    def isMatch(self, source, pattern):
        return self.is_match_helper(source, 0, pattern, 0, {})
    # source 从i开始的后缀能否匹配上，pattern从j开始的后缀
    def is_match_helper(self, source, i, pattern, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]
        # source是空
        if len(source) == i:
            return self.is_empty(pattern[j:])
        if len(pattern) == j:
            return False
        if j + 1 < len(pattern) and pattern[j + 1] == '*':
            matched = self.is_match_char(source[i], pattern[j]) and self.is_match_helper(source, i + 1, pattern, j, self.is_match_helper(source, i, pattern, j + 2, memo))
        else:
            matched = self.is_match_char(source[i], pattern[j]) and self.is_match_helper(source, i + 1, pattern, j + 1, memo)
        memo[(i, j)] = matched
        return matched
    def is_match_char(self, s, p):
        return s == p or p == '.'
    def is_empty(self, pattern):
        if len(pattern) % 2 == 1:
            return False
        for i in range(len(pattern) // 2):
            if pattern[i * 2 + 1] != '*':
                return False
        return True
#主函数
if __name__ == '__main__':
    solution = Solution()
    StringA = "aaa"
    StringB = "aa"
    print("StringA 是：", StringA, "，StringB 是：", StringB, "，它们是否匹配：", solution.isMatch(StringA,StringB))
    StringC = "aab"
    StringD = "c*a*b"
    print("StringC 是：", StringC, "，StringD 是：", StringD, "，它们是否匹配：", solution.isMatch(StringC,StringD))