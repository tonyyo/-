class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
class Solution:
    def binaryTreePaths(self, root):
        if root is None:
            return []
        result = set([])
        self.dfs2(root, [], result)
        return result

    def dfs2(self, node, path, result):
        path.append(str(node.val))  # 如果你只判断到叶子结点，那么应该放在这
        if node.left is None and node.right is None:
            result.append('->'.join(path))
            path.pop()
            return
        self.dfs(node.left, path, result)
        self.dfs(node.right, path, result)
        path.pop()

    def dfs(self, node, path, result): # 找到从node到叶子节点的所有路径
        if node == None: # 不能用这个，不然左右子点都为空的话，那么路径会出现两遍，但这里用的集合，所以可以
            result.add('->'.join(path))
            return
        path.append(str(node.val))
        self.dfs(node.left, path, result)
        self.dfs(node.right, path, result)
        path.pop()


def printTree(root):
    res = []
    if root is None:
        print(res)
    queue = []
    queue.append(root)
    while len(queue) != 0:
        tmp = []
        length = len(queue)
        for i in range(length):
            r = queue.pop(0)
            if r.left is not None:
                queue.append(r.left)
            if r.right is not None:
                queue.append(r.right)
            tmp.append(r.val)
        res.append(tmp)
    print(res)
if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    print("原始二叉树为")
    printTree(root)
    solution = Solution()
    print("后序遍历的结果为", solution.binaryTreePaths(root))