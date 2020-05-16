def numberofDistinctIslands(self, grid):
    rowNum, colNum = len(grid), len(grid[0])
    queue = collections.deque()
    result = []  # 记录岛屿形状，相同的不做重复记录
    for i in range(rowNum):
        for j in range(colNum):
            string = ''  # 初始化岛屿形状
            if grid[i][j] == 1:  # 发现新岛屿
                queue.append([i, j])  # 记录新岛屿的左上角比较点
                grid[i][j] = 0  # 拆除左上角岛屿
                print([i, j])
                while queue:  # 找到了新岛屿就记录它的形状，顺便将新岛屿拆除
                    x, y = queue.popleft()
                    for k in range(4):  # 找出以x，y开始的岛屿其他组成部分
                        nextX, nextY = x + dx[k], y + dy[k]
                        # 如果下一个位置不是岛屿的部分，就换个方向
                        if not (0 <= nextX < rowNum and 0 <= nextY < colNum) or grid[nextX][nextY] != 1:
                            continue
                        # 找到了岛屿的组成部分，加入queue,并不断完善形状
                        else:
                            queue.append([nextX, nextY])  # 找到组成部分
                            grid[nextX][nextX] = 0  # 拆除找到的岛屿
                            string = string + str(nextX - i) + str(nextY - j)  # 记录形状

            if string not in result and string:
                result.append(string)
    return result
