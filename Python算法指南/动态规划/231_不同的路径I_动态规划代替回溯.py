class Solution:
    def c(self, m, n):
        pos = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    pos[0][0] = 1  # 从左上角出发，到达该点的路径为1
                else:  # else 不可获取，不然上面赋的值会被覆盖
                    pos[i][j] = pos[i - 1][j] + pos[i][j - 1]
        return pos[m - 1][n - 1]
#主函数
if __name__ == '__main__':
    m = 3
    n = 3
    print("网格行:{}和列：{}".format(m, n))
    solution = Solution()
    print("路径条数：", solution.c(m, n))