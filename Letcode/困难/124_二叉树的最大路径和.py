import sys


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    res = -sys.maxsize
    def maxPathSum(self, root):
        self.dfs(root)
        return self.res

    def dfs(self, root):  # 返回从root出发的最大路径和，如果为负数，则返回0
        if root == None:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        maxSum = root.val + left + right
        self.res = max(self.res, maxSum)
        return max(0, root.val + max(left, right))
