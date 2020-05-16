class Solution(object):
    def dfs(self, start, destination, maze):
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        flag = False
        rowNum, colNum = len(maze), len(maze[0])
        if start == destination:
            return True
        x, y = start[0], start[1]
        for i in range(4):
            nextX, nextY = x + dx[i], y + dy[i]
            if not (0 <= nextX < rowNum and 0 <= nextY < colNum) or maze[nextX][nextY] == 1:
                continue
            else:
                maze[x][y] = 1
                Flag = self.dfs([nextX, nextY], destination, maze)
                if Flag == True: # 只要拿到了底层的True，立即返回True
                    return True  # 到了最外层循环的时候将会直接返回True
                maze[x][y] = 0
        return False
# 主函数
if __name__ == '__main__':
    maze = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]]
    start = [0, 0]
    destination = [4, 4]
    print("迷宫是：", maze)
    print("初始地点是:", start)
    print("终点是：", destination)
    solution = Solution()
    print(solution.dfs(start, destination, maze))

