class Solution:
    def generatePalindromes(self, s):
        if not s:
            return []
        map = {}
        for c in s:
            map[c] = map.get(c, 0) + 1
        if len(map.keys()) == 1:
            return [s]
        oddCount = 0
        odd = ''
        even = ''
        for key, val in map.items():
            if val % 2 == 1:
                odd = key
                oddCount += 1
            even += key * (val // 2)
        if oddCount > 1:
            return []
        ans = []
        self.permutation('', even, ans, odd)
        return ans
    def permutation(self, substring, s, ans, odd):
        if not s:
            ans.append(substring + odd + substring[::-1])
            return
        for i in range(len(s)):
            self.permutation(substring + s[i], s[:i] + s[i + 1:], ans, odd)

    def is_huiwen(self, s):
        if s == s[::-1]:
            return True
        return False

    def quanpailie(self, s, start, results):
        size = len(s)
        s = list(s)
        if start >= size:
            if self.is_huiwen(s) and "".join(s) not in results: # 字符串转化为列表用join, 用str只能转换数字
                results.append("".join(s))

        for i in range(start, size):
            s[start], s[i] = s[i], s[start]
            self.quanpailie(s, start + 1, results)
            s[start], s[i] = s[i], s[start]
        return results

#主函数
if __name__ == '__main__':
    S = "abc"
    solution = Solution()
    results = []
    print("s = ", S, ",结果是：", solution.quanpailie(S, 0, results))