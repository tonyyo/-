DIRECTIONS = [(1, 0), (-1, 0), (0, -1), (0, 1)]


class Solution(object):
    def hasPath(self, maze, start, destination):
        ans, result = [(start[0], start[1])], []
        self.dfs(maze, start, destination, ans, result)
        return result

    def dfs(self, maze, start, destination, ans, result):
        rowNum, colNum= len(maze), len(maze[0])
        dx, dy= [0, 1, 0, -1], [1, 0, -1, 0]
        x, y = start[0], start[1]
        maze[x][y] = 1
        if x == destination[0] and y == destination[1]:
            result.append((list(ans), len(ans)))
            return
        for i in range(4):
            nextX = x + dx[i]
            nextY = y + dy[i]
            if nextX >=0 and nextY >=0 and nextX < rowNum and nextY < colNum:
                if maze[nextX][nextY] != 1:
                    maze[nextX][nextY] = 1
                    ans.append((nextX, nextY))
                    self.dfs(maze, [nextX, nextY], destination, ans, result)
                    maze[nextX][nextY] = 0
                    ans.pop()
        return
# 主函数
if __name__ == '__main__':
    maze = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]]
    start = [0, 4]
    destination = [4, 4]
    print("迷宫是：", maze)
    print("初始地点是:", start)
    print("终点是：", destination)
    solution = Solution()
    result = solution.hasPath(maze, start, destination)
    for x in result:
        print(x)
