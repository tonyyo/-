import collections


class Solution:
    # 参数map是一个地图
    # 返回一个布尔值，判断是否能到达终点
    def reachEndpoint(self, map):
        rowNum, colNum = len(map), len(map[0])
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        MIN = [[65536 for _ in range(colNum)] for _ in range(rowNum)] # 存取从左上角到达该点的最短路径长度
        MIN[0][0] = 1
        queue = collections.deque()
        queue.append([0, 0])
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nextX, nextY = x + dx[i], y + dy[i]
                if not (0 <= nextX < rowNum and 0 <= nextY < colNum) or map[nextX][nextY] == 0 \
                        or MIN[nextX][nextY] < MIN[x][y] + 1: # 当下一个数更小的时候，没必要加入queue遍历
                    continue
                else:
                    MIN[nextX][nextY] = MIN[x][y] + 1
                    queue.append([nextX, nextY])
        for i in range(rowNum):
            for j in range(colNum):
                if map[i][j] == 9:
                    return MIN[i][j]
        return -1

# 主函数
if __name__ == '__main__':
    map = [[1, 1, 1], [1, 0, 1], [1, 1, 9]]
    print("地图是：", map)
    solution = Solution()
    print("能否到达终点", solution.reachEndpoint(map))
