class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        Y, N = self.subRob(root)
        return max(Y, N)

    def subRob(self, root):  # 从root节点进入 偷root节点和不偷root节点返回的最大金额
        if root == None:
            return 0, 0
        leftY, leftN = self.subRob(root.left)
        rightY, rightN = self.subRob(root.right)
        Y = leftN + rightN + root.val
        N = max(leftY, leftN) + max(rightN, rightY)
        return Y, N
