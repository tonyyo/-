class Solution(object):
    def dfs(self, start, destination, maze, length, MAX):
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        rowNum, colNum = len(maze), len(maze[0])
        if start == destination:
            MAX.append(max(MAX[-1], length + 1)) # 到了终点，要多走一步才能出去
        x, y = start[0], start[1]
        for i in range(4):
            nextX, nextY = x + dx[i], y + dy[i]
            if not (0 <= nextX < rowNum and 0 <= nextY < colNum) or maze[nextX][nextY] == 1:
                continue
            else:
                maze[x][y] = 1
                self.dfs([nextX, nextY], destination, maze, length + 1, MAX)
                maze[x][y] = 0
# 主函数
if __name__ == '__main__':
    maze = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]]
    start = [0, 0]
    destination = [4, 4]
    MAX = [0]
    print("迷宫是：", maze)
    print("初始地点是:", start)
    print("终点是：", destination)
    solution = Solution()
    solution.dfs(start, destination, maze, 1, MAX)
    print(MAX[-1])


