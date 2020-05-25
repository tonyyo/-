class point(object):
    def __init__(self, val, outgoing_edges): # 因为此处举得例子是无向图，所以只需出度即可。
        self.val = val
        self.outgoing_edges = outgoing_edges

class edge(object):
    def __init__(self, startPoint, endPoint):  # 如果有权重的话可以加权重， 单纯就遍历来说，可以只用顶点属性即可
        self.startPoint = startPoint
        self.endPoint = endPoint

class Graph:
# 深度遍历: 针对有向图而言，才会有出度和入度的概念
# 1\求出每个点的所有入度和出度  point的属性：point[point_val, []ingoing_edges, []outgoing_edges];
# 2\求出每条边长的两个端点     edge的属性：edge[edge_val, startPoint, endPoint];
# 3\遍历每个点的出度，由出度找到其下一个点，重复遍历，直到所有的点都遍历完。
    DFSResult = []
    def DFS(self, point, visited_points):
        if point in visited_points:
            return
        for e in point.outgoing_edges:
            self.DFSResult.append(e.val)
            visited_points.append(point)
            self.DFS(e.endPoint, visited_points)
            visited_points.pop(point)

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
                res.append(pos.val)
                for e in point.outgoing_edges:
                    if e not in visited_points:
                        level.append(e)
                        visited_points.append(e)
            res.extend(level)
        return res

if __name__ == '__main__':
    solution = Graph()
    pointF = point('F', None)
    pointE = point('E', {pointF})
    pointD = point('D', {pointE})
    pointC = point('C', {pointE, pointF})
    pointB = point('B', {pointD, pointE})
    pointA = point('A', {pointB, pointC})
    points = {pointA, pointB, pointC, pointD, pointE, pointF}



