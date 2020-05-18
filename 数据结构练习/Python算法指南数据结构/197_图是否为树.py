class Solution:
    def validTree(self, n, edges):
        if n - 1 != len(edges):
            return False
        self.father = {i: i for i in range(n)}
        self.size = n
        for a, b in edges:
            self.union(a, b)
        return self.size == 1
    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.size -= 1
            self.father[root_a] = root_b
    def find(self, node):
        path = []
        while node != self.father[node]:
            path.append(node)
            node = self.father[node]
        for n in path:
            self.father[n] = node
        return node
#主函数
if __name__ == '__main__':
    n = 5
    edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
    print("n = ", n)
    print("edges是：", edges)
    solution = Solution()
    print("图是否是树：", solution.validTree(n, edges))