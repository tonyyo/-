class Solution:
    def minCut(self, s):
        n = len(s)
        f = []
        p = [[False for x in range(n)] for x in range(n)]  # p[i][j]表示在i~j范围内的子字符串是回文数
        # the worst case is cutting by each char
        for i in range(n + 1):
            f.append(n - 1 - i)  # 最差的情况要切n - 1刀,当n=0时
        for i in reversed(range(n)):
            for j in range(i, n):
                if (s[i] == s[j] and (j - i < 2 or p[i + 1][j - 1])):
                    p[i][j] = True
                    f[i] = min(f[i], f[j + 1] + 1)  # 这个最小值是怎么得来的? https://www.jianshu.com/p/188780c84d78
        return f[0]

if __name__ == '__main__':
    s = "aab"
    print("初始字符串：", s)
    solution = Solution()
    print("分割次数：", solution.minCut(s))