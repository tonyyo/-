class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root == None:
            return 0
        left = self.countLevel(root.left)
        right = self.countLevel(root.right)
        if left == right: # 左子树是满树
            return self.countNodes(root.right) + (1 << left) # 根节点和-1抵消了
        else:            # 右子树是满树
            return self.countNodes(root.left) + (1 << right)

    def countLevel(self, root): # 求完全二叉树的层数
        level = 0
        while root:
            level += 1
            root = root.left
        return level