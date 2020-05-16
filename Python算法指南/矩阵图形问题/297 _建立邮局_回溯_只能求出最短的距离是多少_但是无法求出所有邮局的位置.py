import collections

class Solution:
    def shortestDistance(self, grid):
        rowNum, colNum = len(grid), len(grid[0])
        SUM = [[0 for _ in range(colNum)] for _ in range(rowNum)] # 存入各个房子到各个点的最小距离和
        for i in range(rowNum):
            for j in range(colNum):
                if grid[i][j] == 1:
                    queue = collections.deque()
                    queue.append([i, j])
                    MIN = [[65536 for _ in range(colNum)] for _ in range(rowNum)] # 距每个房子的最小距离数组
                    MIN[i][j] = 0 # 初始化
                    self.dfs(grid, queue, MIN)
                    print(MIN)
                    for k in range(rowNum): # 紧记超过双重循环不要再用i和j了
                        for l in range(colNum):
                            SUM[k][l] += MIN[k][l]
        return SUM

    def dfs(self, grid, queue, MIN):
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        rowNum, colNum = len(grid), len(grid[0])
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nextX, nextY = x + dx[i], y + dy[i]     # 是墙的话不能构建邮局，房子的地方可以构建
                if not (0 <= nextX < rowNum and 0 <= nextY < colNum) or grid[nextX][nextY] == 2 \
                        or MIN[nextX][nextY] < MIN[x][y] + 1:  # 不会再回到那个更小值的地方
                    continue
                else:
                    queue.append([nextX, nextY]) # 这是遍历的核心
                    MIN[nextX][nextY] = MIN[x][y] + 1 # 这是计算的核心


if __name__ == '__main__':
    grid = [[0, 1, 0, 0, 0], [1, 0, 0, 2, 1], [0, 1, 0, 0, 0]]
    print("网格是：", grid)
    solution = Solution()
    print("最近的距离是：", solution.shortestDistance(grid))
