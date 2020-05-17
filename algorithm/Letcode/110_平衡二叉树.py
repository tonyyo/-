class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    flag = True
    def isBalanced(self, root):
        self.dfs(root)
        return self.flag

    def dfs(self, root):  # 返回以root为根节点的深度
        if root == None:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        if abs(left - right) > 1:
            self.flag = False
        return 1 + max(left, right)
