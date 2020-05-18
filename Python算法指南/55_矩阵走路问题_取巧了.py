class Solution:
    def getBestRoad(self, grid):
        rowNum, colNum = len(grid), len(grid[0])
        count = 0
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        direct = 0
        x, y = 0, 0
        ans = []
        while x != rowNum - 1 or y != colNum -1:
            nextX = x + dx[direct]
            nextY = y + dy[direct]
            if nextX >= 0 and nextY >= 0 and nextX < rowNum and nextY < colNum and grid[nextX][nextY] == 0:
                x, y = nextX, nextY
            elif  nextX < rowNum and nextY < colNum and grid[nextX][nextY] == 1 and 1 not in ans:
                x, y = nextX, nextY
            else:
                if direct == 0:
                    x += 1
                else:
                    y += 1
                direct = (direct + 1) % 2
            ans.append(grid[x][y])
            count += 1
        return count

# 主函数
if __name__ == '__main__':
    a = [[0, 1, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 0], [1, 1, 1, 1, 0]]
    print("地图是：", a)
    solution = Solution()
    print("最少要走：", solution.getBestRoad(a))

# class node:
#     def __init__(self, a=0, b=0, i=0, s=0):
#         self.x = a
#         self.y = b
#         self.i = i
#         self.step = s
# class Solution:
#     def getBestRoad(self, grid):
#         direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]  # 右左下上四个方向
#         n = len(grid)  # n时行数
#         m = len(grid[0]) # m是列数
#         # print(n,m)
#         # 三维矩阵, 存的是坐标, 记录的是
#         visit = [[[0 for i in range(2)] for i in range(m)] for i in range(n)]
#         p = []
#         if (grid[0][0] == 0):
#             new = node(0, 0, 0, 0)  # 创建0节点
#             visit[0][0][0] = 1
#         else:
#             new = node(0, 0, 1, 0)   # 创建1节点
#         p.append(new)
#         flag = -1
#         visit[0][0][1] = 1
#         cnt = 0
#         while cnt < len(p):
#             a = p[cnt]
#             cnt += 1
#             # print(a.x,a.y,a.i,a.step)
#             if a.x == n - 1 and a.y == m - 1:  # 如果到了右下角节点, 那么返回步数
#                 flag = a.step
#                 break
#             else:
#                 for i in range(0, 4):
#                     new_x = a.x + direction[i][0]  # 试探步
#                     new_y = a.y + direction[i][1]
#                     if new_x <= n - 1 and new_x >= 0 and new_y <= m - 1 and new_y >= 0:  # 如果没有越界
#                         if grid[new_x][new_y] == 0 and visit[new_x][new_y][a.i] == 0: # 如果有路
#                             visit[new_x][new_y][a.i] = 1
#                             visit[new_x][new_y][1] = 1
#                             p.append(node(new_x, new_y, a.i, a.step + 1))
#                     if grid[new_x][new_y] == 1 and a.i == 0 and visit[new_x][new_y][1] == 0:
#                             visit[new_x][new_y][1] = 1
#                             p.append(node(new_x, new_y, 1, a.step + 1))
#         return flag
