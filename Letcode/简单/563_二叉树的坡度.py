class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    tilt = 0
    def findTilt(self, root):
        self.dfs(root)
        return self.tilt

    def dfs(self, root): # 返回该树的节点之和
        if root == None:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        self.tilt += abs(left - right)
        return root.val + left + right