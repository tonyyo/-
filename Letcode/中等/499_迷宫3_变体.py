class Solution:
    def wallsAndGates(self, rooms):
        if len(rooms) == 0:
            return []
        M, N = len(rooms), len(rooms[0])
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        import collections
        queue = collections.deque()
        exit = []
        import sys
        for i in range(M):
            for j in range(N):
                if rooms[i][j] == '*':
                    rooms[i][j] = sys.maxsize
                if rooms[i][j] == '#':
                    rooms[i][j] = -1
                if rooms[i][j] == 'S':
                    queue.append((i, j))
                    rooms[i][j] = 0
                if rooms[i][j] == 'E':
                    exit.append((i, j))
                    rooms[i][j] = sys.maxsize
        while queue:
            x, y = queue.popleft()
            if (x, y) in exit:
                return rooms[x][y]
            for i in range(4):
                nextX, nextY = x + dx[i], y + dy[i]
                if not (0 <= nextX < M and 0 <= nextY < N) or rooms[nextX][nextY] <= rooms[x][y] + 1:
                    continue
                queue.append((nextX, nextY))
                rooms[nextX][nextY] = rooms[x][y] + 1
        return -1

           #主函数
if __name__ == '__main__':
    grid = [
        ['S', '*', '*'],
        ['*', 'E', 'E'],
        ['*', '*', '*']
    ]
    print("迷宫是：", grid)
    solution = Solution()
    print("离开迷宫需要的最少时间是：", solution.wallsAndGates(grid))