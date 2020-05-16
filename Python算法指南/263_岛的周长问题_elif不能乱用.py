class Solution:
    def islandPerimeter(self, grid):
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    result += self.checkSingleIsland(i, j, grid)
        return result
    def checkSingleIsland(self, i, j, grid):  # https://www.jianshu.com/p/c149466ca883
        top = 1 - grid[i - 1][j] if i - 1 >= 0 else 1
        bottom = 1 - grid[i + 1][j] if i + 1 < len(grid) else 1
        left = 1 - grid[i][j - 1] if j - 1 >= 0 else 1
        right = 1 - grid[i][j + 1] if j + 1 < len(grid[0]) else 1
        return top + bottom + left + right

    def islandPerimeter1(self, grid):
        rowNum = len(grid)
        colNum = len(grid[0])
        perimerter = 0
        for i in range(rowNum):
            for j in range(colNum):
                if grid[i][j] == 1:
                    perimerter += 4
                    if i - 1 >= 0 and grid[i - 1][j] == 1:
                        perimerter -= 2
                    if j - 1 >= 0 and grid[i][j - 1] == 1: # 这里不能用elif
                        perimerter -= 2
        return perimerter
#主函数

if __name__ == "__main__":
    grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
    #创建对象
    solution = Solution()
    print("初始化的数组", grid)
    print("岛的周长是：", solution.islandPerimeter1(grid))