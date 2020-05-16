import collections

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


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
                    if i - 1 >= 0 and grid[i - 1][j] == 1: # 那么两个正方形都少一边，所以减2
                        perimerter -= 2
                    if j - 1 >= 0 and grid[i][j - 1] == 1:  # 这里不能用elif
                        perimerter -= 2
        return perimerter

    def islandPerimeter2(self, grid):
        rowNum, colNum = len(grid), len(grid[0])
        count = 0
        flag = False # 设置标志位，防止全局遍历。
        for i in range(rowNum):
            for j in range(colNum):
                queue = collections.deque()
                if grid[i][j] == 1:
                    queue.append([i, j])
                    while queue:
                        x, y = queue.popleft()
                        grid[x][y] = 2 # 经过的岛屿部分不要再经过了
                        count += 4
                        if x - 1 >= 0 and grid[x - 1][y] != 0: # 只要不临近水域就减2
                            count -= 2
                        if y - 1 >= 0 and grid[x][y - 1] != 0:
                            count -= 2
                        for k in range(4):
                            nextX, nextY = x + dx[k], y + dy[k]
                            if not (0 <= nextX < rowNum and 0 <= nextY < colNum) \
                                    or grid[nextX][nextY] != 1:
                                continue
                            else:
                                queue.append([nextX, nextY])
                    flag = True
                if flag:
                    break
            if flag:
                break
        return count

# 主函数

if __name__ == "__main__":
    grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
    # 创建对象
    solution = Solution()
    print("初始化的数组", grid)
    print("岛的周长是：", solution.islandPerimeter1(grid))
    print("岛的周长是：", solution.islandPerimeter2(grid))
