import collections
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
DIRECTIONS = []
from collections import deque
class Solution:
    def numberofDistinctIslands1(self, grid):
        if not grid:
            return 0
        queue, check, ans = deque(), set(), 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    path = " "
                    queue.append((i, j))
                    grid[i][j] = 0
                    while queue:
                        x, y = queue.popleft()
                        for dx, dy in DIRECTIONS:
                            new_x, new_y = x + dx, y + dy
                            if self.is_valid(grid, new_x, new_y):
                                queue.append((new_x, new_y))
                                grid[new_x][new_y] = 0
                                path += str(new_x - i) + str(new_y - j)
                    if path not in check:
                        ans += 1
                        check.add(path)
        print(path)
        return ans
    def is_valid(self, grid, x, y):
        row, col = len(grid), len(grid[0])
        return x >= 0 and x < row and y >= 0 and y < col and grid[x][y] == 1

    def inbound(self, grid, x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0])

    def numberofDistinctIslands(self, grid):
        rowNum = len(grid)
        colNum = len(grid[0])
        count, ans, queue = 0, [], collections.deque()
        for i in range(rowNum):
            for j in range(colNum):
                path = ""
                if grid[i][j] == 1:
                    queue.append([i, j])
                    grid[i][j] = 0
                    while queue:
                        tempList = queue.popleft()
                        for k in range(4):
                            nextX = tempList[0] + dx[k]
                            nextY = tempList[1] + dy[k]
                            if not self.inbound(grid, nextX, nextY) or grid[nextX][nextY] != 1:
                                continue
                            grid[nextX][nextY] = 0
                            queue.append([nextX, nextY])
                            path = path + str(nextX - i) + str(nextY - j)
                if path not in ans and path:
                    ans.append(path)
        return ans

                #主函数
if __name__ == '__main__':
    grid = [
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1],
        [0, 0, 0, 1, 1]
    ]
    print("矩阵是：", grid)
    solution = Solution()
    print("不同岛屿个数是：", solution.numberofDistinctIslands(grid))