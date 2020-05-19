class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution():
    def mergeTrees(self, t1, t2):  # 合并t1和t2两棵二叉树
        if t1 == None:
            return t2
        if t2 == None:
            return t1
        root = TreeNode(t1.val + t2.val)
        root.left = self.mergeTrees(t1.left, t2.left)
        root.right = self.mergeTrees(t1.right, t2.right)
        return root

