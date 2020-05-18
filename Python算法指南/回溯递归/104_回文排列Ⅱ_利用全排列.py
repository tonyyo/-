class Solution:
    def quanpailie(self, s, start, results):
        size = len(s)
        s = list(s)  # 字符串转字符串数组
        if start >= size:
            string = "".join(s)  # 字符串数组转字符串
            if s == s[::-1] and string not in results: # 字符串转化为列表用join, 用str只能转换数字
                results.append(string)
        for i in range(start, size):
            s[start], s[i] = s[i], s[start]
            self.quanpailie(s, start + 1, results)
            s[start], s[i] = s[i], s[start]

#主函数
if __name__ == '__main__':
    S = "aabbc"
    solution = Solution()
    results = []
    solution.quanpailie(S, 0, results)
    print(results)