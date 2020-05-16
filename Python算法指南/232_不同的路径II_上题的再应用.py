class Solution:
    def c(self, obstacleGrid):
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        mp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                mp[i + 1][j + 1] = obstacleGrid[i][j]

        for i in range(1, len(mp)):
            for j in range(1, len(mp[0])):
                if i == 1 and j == 1:
                    mp[i][j] = 1
                elif mp[i][j] == 1:
                    mp[i][j] = 0
                else:
                    mp[i][j] = mp[i - 1][j] + mp[i][j - 1]
        for x in mp:
            print(x)
        return mp[m][n]
#主函数
if __name__ == '__main__':
    obstacleGrid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    print("初始网格：")
    for i in range(0, len(obstacleGrid)):
        print(obstacleGrid[i])
    solution = Solution()
    print("路径条数：", solution.c(obstacleGrid))