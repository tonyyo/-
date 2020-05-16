class Solution:
     def c(self, obstacleGrid):
        rowNum, colNum = len(obstacleGrid), len(obstacleGrid[0])
        pos = [[0 for _ in range(colNum)] for _ in range(rowNum)]
        for i in range(rowNum):
            for j in range(colNum):
                if i == 0 and j == 0:
                    pos[i][j] = 1
                else:
                    if obstacleGrid[i - 1][j] == 1:
                        pos[i - 1][j] = 0 # 上方为障碍物时，从上方来的路径为0
                    if obstacleGrid[i][j - 1] == 1:
                        pos[i][j - 1] = 0 # 同上
                    pos[i][j] = pos[i - 1][j] +  pos[i][j - 1]
        return pos[rowNum - 1][colNum - 1]
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