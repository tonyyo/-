class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        # if root == None and sum == 0:  不能这么做，因为加入二叉树有正有负，sum == 0，那么无论如何都是True
        #     return True
        if root == None: return False  # 排除根节点为空
        if not root.left and not root.right:
            return root.val == sum
        Left = self.hasPathSum(root.left, sum - root.val)
        Right = self.hasPathSum(root.right, sum - root.val)
        return Left or Right