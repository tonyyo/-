class Solution:  # https://www.jianshu.com/p/50af9094a2ac
    def backPack(self, m, A):
        n = len(A)
        f = [[False] * (m + 1) for _ in range(n + 1)]
        f[0][0] = True
        for i in range(1, n + 1):
            f[i][0] = True
            for j in range(1, m + 1):
                if j >= A[i - 1]:
                    f[i][j] = f[i - 1][j] or f[i - 1][j - A[i - 1]]
                else:
                    f[i][j] = f[i - 1][j]
        for i in range(m, -1, -1):
            if f[n][i]:
                return i
        return 0
#主函数
if __name__ == '__main__':
    m = 11
    A = [2, 3, 5, 7]
    print("背包大小：", m)
    print("每个物品大小：", A)
    solution = Solution()
    print("最多装满的空间：", solution.backPack(m, A))