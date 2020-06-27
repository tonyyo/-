class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        mp = [[0] * n for _ in range(m)]
        mp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:  # 遇到障碍物，路径清0
                    mp[i][j] = 0
                elif i == 0 and j == 0:
                    mp[i][j] = 1
                elif i == 0:
                    mp[i][j] = mp[i][j - 1]
                elif j == 0:
                    mp[i][j] = mp[i - 1][j]
                else:
                    mp[i][j] = mp[i - 1][j] + mp[i][j - 1]
        return mp[m - 1][n - 1]
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
    print("路径条数：", solution.uniquePathsWithObstacles(obstacleGrid))