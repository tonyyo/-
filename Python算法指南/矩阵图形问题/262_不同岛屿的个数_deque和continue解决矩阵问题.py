import collections
dx = [0, 1, 0, -1] # 放在这里定义全局变量。
dy = [1, 0, -1, 0]
class Solution:
    def numberofDistinctIslands1(self, grid):
        rowNum = len(grid)
        colNum = len(grid[0])
        ans, queue = [], collections.deque()
        for i in range(rowNum):
            for j in range(colNum):
                path = ""
                if grid[i][j] == 1:
                    queue.append([i, j])
                    grid[i][j] = 0
                    while queue:
                        x, y = queue.popleft()
                        for k in range(4):
                            nextX = x + dx[k]
                            nextY = y + dy[k]
                            if not (0 <= nextX < rowNum and 0 <= nextY < colNum) or grid[nextX][nextY] != 1:
                                continue
                            grid[nextX][nextY] = 0
                            queue.append([nextX, nextY])
                            path = path + str(nextX - i) + str(nextY - j)
                if path not in ans and path:
                    ans.append(path)
        return ans

        # 主函数

    def numberofDistinctIslands(self, grid):
        rowNum = len(grid)
        colNum = len(grid[0])
        ans, queue = [], collections.deque()
         # 记录岛屿形状，相同的不做重复记录
        for i in range(rowNum):
            for j in range(colNum):
                path = "" # 初始化岛屿形状
                if grid[i][j] == 1: # 发现新岛屿
                    queue.append([i, j]) # 记录新岛屿的左上角比较点
                    grid[i][j] = 0  # 拆除左上角岛屿
                    while queue: # 找到了新岛屿就记录它的形状，顺便将新岛屿拆除
                        x, y = queue.popleft()
                        for k in range(4): # 找出以x，y开始的岛屿其他组成部分
                            nextX = x + dx[k]
                            nextY = y + dy[k]
                            # 如果下一个位置不是岛屿的部分，就换个方向
                            if not (0 <= nextX < rowNum and 0 <= nextY < colNum) or grid[nextX][nextY] != 1:
                                continue
                            # 找到了岛屿的组成部分，加入queue,并不断完善形状
                            grid[nextX][nextX] = 0  # 拆除找到的岛屿
                            queue.append([nextX, nextY]) # 找到组成部分
                            path = path + str(nextX - i) + str(nextY - j)  # 记录形状
                if path not in ans and path:
                        ans.append(path)
        return ans

if __name__ == '__main__':
    grid = [
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1],
        [0, 0, 0, 1, 1]
    ]
    grid1 = [
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1],
        [0, 0, 0, 1, 1]
    ]
    print("矩阵是：", grid)
    solution = Solution()
    print("不同岛屿个数是：", solution.numberofDistinctIslands(grid))
    print("不同岛屿个数是：", solution.numberofDistinctIslands1(grid1))
