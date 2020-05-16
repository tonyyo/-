class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
class Solution:
    def portal2(self, grid):
        n = len(grid)
        m = len(grid[0])
        import sys
        record = [[sys.maxsize for _ in range(m)] for i in range(n)]
        for i in range(0, n):
            for j in range(0, m):
                if (grid[i][j] == 'S'):
                    source = Point(i, j)
        record[source.x][source.y] = 0
        import queue
        q = queue.Queue(maxsize=n * m)
        q.put(source)
        d = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        while not q.empty():
            head = q.get()
            for dx, dy in d:
                x, y = head.x + dx, head.y + dy
                if 0 <= x < n and 0 <= y < m and grid[x][y] != '#' and \
                        record[head.x][head.y] + 1 < record[x][y]:
                    record[x][y] = record[head.x][head.y] + 1
                    if grid[x][y] == 'E':
                        return record[x][y]
                    q.put(Point(x, y))
        return -1

    def portal(self, grid):
        rowNum = len(grid)
        colNum = len(grid[0])
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        import  queue
        queue = queue.Queue()
        endX, endY = 0, 0
        for i in range(rowNum):
            for j in range(colNum):
                if grid[i][j] == 'S':
                    queue.put(Point(i, j))
                    grid[i][j] = 0
                if grid[i][j] == '*':
                    grid[i][j] = 65536
                if grid[i][j] == "E":
                    grid[i][j] = 65536
                    endX, endY = i, j
        while not queue.empty():
            tempPoint = queue.get()
            x, y = tempPoint.x, tempPoint.y
            for i in range(4):
                nextX = x + dx[i]
                nextY = y + dy[i]
                if nextX < 0 or nextY < 0 or nextX >= rowNum or nextY >= colNum or grid[nextX][nextY] == '#' or grid[nextX][nextY] < grid[x][y] + 1:
                    continue
                grid[nextX][nextY] = grid[x][y] + 1
                if nextX == endX and nextY == endY:
                    break
                queue.put(Point(nextX, nextY))
        return grid[endX][endY]

           #主函数
if __name__ == '__main__':
    grid = [
        ['S', '*', '*'],
        ['*', '*', 'E'],
        ['*', '*', '*']
    ]
    print("迷宫是：", grid)
    solution = Solution()
    print("离开迷宫需要的最少时间是：", solution.portal(grid))