class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
     def maxSumBST(self, root: TreeNode) -> int:
         self.maxSum = 0  # 保证了就算全为负数时，也能返回正确结果0
         self.dfs(root)
         return self.maxSum

     def dfs(self, root):
         if root == None:
             return 0, 5e4, -5e4  # 保证了空节点绝对是一颗二叉搜索树
         leftSum, left_minVal, left_maxVal = self.dfs(root.left)
         rightSum, right_minVal, right_maxVal = self.dfs(root.right)  # 自底向上应采取后续遍历
         if left_maxVal < root.val and root.val < right_minVal:
             sum = root.val + leftSum + rightSum
             self.maxSum = max(self.maxSum, sum)
             return sum, min(root.val, left_minVal), max(root.val, right_maxVal)
         return 0, -5e4, 5e4




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
