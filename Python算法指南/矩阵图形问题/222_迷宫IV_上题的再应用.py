import collections

class Solution:
    def portal(self, grid):
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        queue = collections.deque()
        rowNum, colNum = len(grid), len(grid[0])
        MIN = 65536
        for i in range(rowNum):
            for j in range(colNum):
                if grid[i][j] == 'S':
                    queue.append([i, j])
                    grid[i][j] = 0
                if grid[i][j] == '*':
                    grid[i][j] = 65536
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nextX, nextY = x + dx[i], y + dy[i]
                # 当到了出口之一时，记录最小值
                if 0 <= nextX < rowNum and 0 <= nextY < colNum and grid[nextX][nextY] == 'E':
                    MIN = min(MIN, grid[x][y] + 1)
                # 当出界或者遇到障碍物，或者下一个值本来就很小时，换个方向
                elif not (0 <= nextX < rowNum and 0 <= nextY < colNum) or grid[nextX][nextY] == '#' \
                        or grid[nextX][nextY] <= grid[x][y] + 1:
                    continue
                else:
                    grid[nextX][nextY] = grid[x][y] + 1
                    # 加入遍历序列
                    queue.append([nextX, nextY])
        return  MIN



if __name__ == '__main__':
    grid = [
        ['S', 'E', '*'],
        ['*', '*', 'E'],
        ['*', '*', '*']
    ]
    print("迷宫是：", grid)
    solution = Solution()
    print("离开迷宫需要的最少时间是：", solution.portal(grid))