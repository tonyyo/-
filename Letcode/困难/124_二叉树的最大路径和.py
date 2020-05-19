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

    def dfs(self, root):    # 返回从root节点往下的最大路径和, 类似求最大深度, equals max(root.val , root.val + 左节点的最大路径和 + 右节点的最大路径和）  因为左右节点的最大路径和可能为0， 那么还不如不加
        if root == None:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        maxSum = root.val + max(0, left) + max(0, right)  # 如果为0， 还不如不加
        self.res = max(self.res, maxSum)
        return root.val + max(0, max(left, right))
