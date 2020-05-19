class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxSumBST(self, root: TreeNode) -> int:
        self.max_value = 0
        self.helper(root)
        return self.max_value

    def helper(self, root):
        # 返回三个变量
        # 分别为【以当前节点为根节点的二叉搜索树的键值和】,【上界】,【下界】
        if not root:
            return 0, 5e4, -5e4
        value1, min_value1, max_value1 = self.helper(root.left)
        value2, min_value2, max_value2 = self.helper(root.right)
        if max_value1 < root.val and min_value2 > root.val:
            # 满足二叉搜索树条件
            self.max_value = max(self.max_value, value1 + value2 + root.val)
            return value1 + value2 + root.val, min(min_value1, root.val), max(max_value2, root.val)
        # 说明该节点无法构成二叉搜索树，返回恒不成立的条件，一直返回到顶
        return root.val, -5e4, 5e4

    # def maxSumBST(self, root: TreeNode) -> int:
    #     self.dfs(root, root.val)
    #     return self.maxSum
    #
    # def dfs(self, root, sum):
    #     self.maxSum = max(self.maxSum, sum)
    #     if root == None:
    #         return
    #     if root.left == None and root.right == None:
    #         return
    #     else:
    #         if root.left == None:
    #             if root.right.val > root.val:
    #                 sum += root.right.val
    #                 self.dfs(root.right, sum)
    #             else:
    #                 self.maxSum = 0
    #                 self.dfs(root.right, root.right.val)
    #         elif root.right == None:
    #             if root.left.val < root.val:
    #                 sum += root.left.val
    #                 self.dfs(root.left, sum)
    #             else:
    #                 self.maxSum = 0
    #                 self.dfs(root.left, root.left.val)
    #         elif root.left.val < root.val and root.right.val > root.val:
    #             sum = sum + root.left.val + root.right.val
    #             self.dfs(root.left, sum)
    #             self.dfs(root.right, sum)
    #         else:
    #             self.maxSum = 0
    #             self.dfs(root.left, root.left.val)
    #             self.dfs(root.right, root.right.val)
