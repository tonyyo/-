class Solution:
    def uniquePaths(self, m, n):
        mp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if (i == 0 or j == 0):  # 第一行和第一列都只有一条路径可达
                    mp[i][j] = 1
                else:
                    mp[i][j] = mp[i - 1][j] + mp[i][j - 1]
        return mp[m - 1][n - 1]
#主函数
if __name__ == '__main__':
    m = 3
    n = 3
    print("网格行:{}和列：{}".format(m, n))
    solution = Solution()
    print("路径条数：", solution.uniquePaths(m, n))