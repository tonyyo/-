class point(object):
    def __init__(self, val, outgoing = []): # outgoing为节点的出度集合, 装的是点
        self.val = val
        self.outgoing = outgoing

class Graph:
    def DFS(self, point, visited_points):   # 模仿二叉树的深度遍历
        if point in visited_points:   # 因为不可能为空
            return
        visited_points.append(point)
        for point in point.outgoing:  # 模仿遍历左右字树
            self.DFS(point, visited_points)

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
                for e in pos.outgoing:
                    if e not in visited_points:  # 模仿遍历左右子树
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
    visited_points = []
    solution.DFS(pointA, visited_points)
    for node in visited_points:
        print(node.val, end=" ")
    print(solution.BFS(pointA))




