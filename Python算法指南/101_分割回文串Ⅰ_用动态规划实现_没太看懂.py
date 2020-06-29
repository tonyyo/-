class Solution:
    def partition(self, s):
        result = []
        self.backtrack(s, [], result)
        return result

    def backtrack(self, s, temp, result):
        if s == "":  #  s[N:N]
            result.append(temp[:])
            return
        N = len(s)
        for i in range(N):
            if not self.isHuiwen(s[:i + 1]):  # s[0:0] == ""
                continue
            self.backtrack(s[i + 1:], temp + [s[:i + 1]], result)

    def isHuiwen(self, s):
        return s[::-1] == s

if __name__ == '__main__':
    s = "aab"
    print("初始字符串：", s)
    solution = Solution()
    print("分割次数：", solution.partition(s))