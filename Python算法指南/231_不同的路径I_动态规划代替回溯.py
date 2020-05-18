class Solution:
    def c1(self, m, n):
        mp = {}
        for i in range(m):
            for j in range(n):
                if (i == 0 or j == 0):
                    mp[(i, j)] = 1
                else:
                    mp[(i, j)] = mp[(i - 1, j)] + mp[(i, j - 1)]  # 元组不可变, 所以可以作为key
        return mp[(m - 1, n - 1)]

    def c(self, m, n):  # 因为只有上下两个方向, 且只问条数, 所以可以用动态规划
        mp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, len(mp)):
            for j in range(1, len(mp[0])):
                if i == 1 and j == 1:
                    mp[i][j] = 1
                else:
                    mp[i][j] = mp[i - 1][j] + mp[i][j - 1]
        for x in mp:
            print(x)
        return mp[m][n]
#主函数
if __name__ == '__main__':
    m = 3
    n = 3
    print("网格行:{}和列：{}".format(m, n))
    solution = Solution()
    print("路径条数：", solution.c(m, n))