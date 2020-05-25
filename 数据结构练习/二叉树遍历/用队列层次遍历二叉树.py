class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
class Solution():
    def buildTree(self, start, A):  # 从start处开始构造普通二叉树，一般从0开始
        if start >= len(A):
            return
        node = TreeNode(A[start])
        node.left = self.buildTree(2 * start + 1, A)  # 下一个节点为2 * start + 1
        node.right = self.buildTree(2 * start + 2, A)
        return node

    def bfs(self, root):
        res, queue = [], []
        queue.append(root)
        while queue:
            level = []
            length = len(queue)
            for _ in range(length):
                pos = queue.pop(0)
                level.append(pos.val)
                if pos.left:
                    queue.append(pos.left)
                if pos.right:
                    queue.append(pos.right)
            res.append(level)
        return res

if __name__ == '__main__':
    solution = Solution()
    A = [1, 2, 3, 4, 5]
    root = solution.buildTree(0, A)
    print(solution.bfs(root))
