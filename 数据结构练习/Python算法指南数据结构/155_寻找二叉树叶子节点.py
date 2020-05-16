class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
class Solution:
#参数root是一个二叉树的根节点
#返回值是收集并移除的所有叶子节点
    def findLeaves(self, root):
        ans = []
        self.depth = {}
        maxDepth = self.dfs(root)
        for i in range(1, maxDepth + 1):
            ans.append(self.depth.get(i))
        return ans
    def dfs(self, node):
        #寻找树深度
        if node is None:
            return 0
        d = max(self.dfs(node.left), self.dfs(node.right)) + 1
        if d not in self.depth:
            self.depth[d] = []
        self.depth[d].append(node.val)
        return d
# 主函数
if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    solution = Solution()
    print("收集的节点是：", solution.findLeaves(root))