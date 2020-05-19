import collections


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    max = 0
    def longestZigZag(self, root: TreeNode) -> int:
        self.dfs(root, 0, 0)
        self.dfs(root, 1, 0)
        return self.max

    def dfs(self, root, dir, length):  # 返回以root为起始节点，以dir方向的路径
        if root == None:
            return
        self.max = max(self.max, length)
        if dir == 0:
            self.dfs(root.left, 1, length + 1)
            self.dfs(root.right, 0, 1)   # 这句可以很好的避免再次进行前序遍历，非常精华。
        else:
            self.dfs(root.right, 0, length + 1)
            self.dfs(root.left, 1, 1)



    def buildBTree(self, List):
        if len(List) == 1:
            return TreeNode(List[0])
        mid = (len(List) - 1) // 2
        root = TreeNode(List[mid])
        root.left = self.buildBTree(List[:mid])
        root.right = self.buildBTree(List[mid + 1:])
        return root

    def levelOrder(self, root):
        result = []
        queue = collections.deque()
        queue.append(root)
        while queue:
            tmp = []
            length = len(queue)
            for _ in range(length):
                pos = queue.popleft()
                tmp.append(pos.val)
                if pos.left is not None:
                    queue.append(pos.left)
                if pos.right is not None:
                    queue.append(pos.right)
            result.append(tmp)
        return result

if __name__ == '__main__':
    solution = Solution()
    List = [1, 2, 3, 4, 5, 6, 7]
    root = solution.buildBTree(List)
    print(solution.levelOrder(root))
    print(solution.longestZigZag(root))
