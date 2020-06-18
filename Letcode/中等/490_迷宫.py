class Solution(object):
    def dfs(self, start, destination, maze):
        if len(maze) == 0:
            return False
        M, N = len(maze), len(maze[0])
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        import collections
        queue = collections.deque()
        queue.append(start)
        route = []
        while queue:
            x, y = queue.popleft()
            route.append((x, y))
            maze[x][y] = 1
            if x == destination[0] and y == destination[1]:
                print(route)
                return True
            for i in range(4):
                nextX, nextY = x + dx[i], y + dy[i]
                if not (0 <= nextX < M and 0 <= nextY < N) or maze[nextX][nextY] == 1:
                    continue
                if (nextX, nextY) not in queue:
                    queue.append((nextX, nextY))
        return False

# 主函数
if __name__ == '__main__':
    maze = [[0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0],
            [1, 1, 0, 1, 1],
            [0, 0, 0, 0, 0]]
    start = (0, 0)
    destination = (4, 4)
    print("迷宫是：", maze)
    print("初始地点是:", start)
    print("终点是：", destination)
    solution = Solution()
    print(solution.dfs(start, destination, maze))