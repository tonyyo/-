class point(object):
    def __init__(self, val, outgoing_edges): # 不知不觉采用的是邻接表的遍历
        self.val = val
        self.outgoing_edges = outgoing_edges

class edge(object):
    def __init__(self, startPoint, endPoint):  # 如果采用的是
        self.startPoint = startPoint
        self.endPoint = endPoint

class Graph:
    DFSResult = []
    def DFS(self, point, visited_points):   # 模仿二叉树的深度遍历
        if point in visited_points:
            return
        self.DFSResult.append(point.val)
        visited_points.append(point)
        for e in point.outgoing_edges:
            self.DFS(e, visited_points)

# 广度遍历：
# 相比于二叉树的层次遍历，就多了访问数组这一概念
    def BFS(self, point):
        res, queue, visited_points = [], [], []
        queue.append(point)
        visited_points.append(point)
        while queue:
            level = []
            length = len(queue)
            for _ in range(length):
                pos = queue.pop(0)
                level.append(pos.val)
                for e in pos.outgoing_edges:
                    if e not in visited_points:
                        queue.append(e)
                        visited_points.append(e)
            res.extend(level)
        return res

if __name__ == '__main__':
    solution = Graph()
    pointF = point('F', [])
    pointE = point('E', [pointF])
    pointD = point('D', [pointE])
    pointC = point('C', [pointE, pointF])
    pointB = point('B', [pointD, pointE])
    pointA = point('A', [pointB, pointC])
    # solution.DFS(pointA, [])
    # print(solution.DFSResult)
    print(solution.BFS(pointA))




