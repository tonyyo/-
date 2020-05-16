import queue as Queue
DIRECTIONS = [(-1, 0), (1, 0), (0, 1), (0, -1)]
SAPCE = 1
OBSTACLE = 0
ENDPOINT = 9
class Solution:
#参数map是一个地图
#返回一个布尔值，判断是否能到达终点
    def reachEndpoint(self, map):
        if not map or not map[0]:
            return False
        self.n = len(map)
        self.m = len(map[0])
        queue = Queue.Queue()
        queue.put((0, 0))
        while not queue.empty():
            curr = queue.get()
            for i in range(4):
                x = curr[0] + DIRECTIONS[i][0]
                y = curr[1] + DIRECTIONS[i][1]
                if not self.isValid(x, y, map):
                    continue
                if map[x][y] == ENDPOINT:
                    return True
                queue.put((x, y))
                map[x][y] = OBSTACLE
        return False
    def isValid(self, x, y, map):
        if x < 0 or x >= self.n or y < 0 or y >= self.m:
            return False
        if map[x][y] == OBSTACLE:
            return False
        return True
#主函数
if __name__ == '__main__':
    map = [[1, 1, 1], [1, 1, 1], [1, 1, 9]]
    print("地图是：", map)
    solution = Solution()
    print("能否到达终点", solution.reachEndpoint(map))