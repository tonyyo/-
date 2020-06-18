import sys


class Solution(object):
    def dfs(self, start, destination, maze):
        if len(maze) == 0:
            return False
        M, N = len(maze), len(maze[0])
        visit = [[sys.maxsize] * N for _ in range(M)]
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        import collections
        queue = collections.deque()
        queue.append(start)
        visit[start[0]][start[1]] = 0
        route = []
        while queue:
            x, y = queue.popleft()
            route.append((x, y))
            maze[x][y] = 1
            if x == destination[0] and y == destination[1]:
                return visit[destination[0]][destination[1]]
            for i in range(4):
                nextX, nextY = x + dx[i], y + dy[i]
                if not (0 <= nextX < M and 0 <= nextY < N) or maze[nextX][nextY] == 1 or visit[nextX][nextY] <= visit[x][y] + 1:
                    continue
                if (nextX, nextY) not in queue:
                    queue.append((nextX, nextY))
                visit[nextX][nextY] = visit[x][y] + 1
        return 0

# 主函数
if __name__ == '__main__':
    maze = [[0, 0, 0, 0, 0],
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