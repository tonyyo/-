class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
class Solution:
    def isValidBST(self, root):
        self.lastVal = None
        self.isBST = True
        self.validate(root)
        return self.isBST
    def validate(self, root):
        if root is None:
            return
        self.validate(root.left)
        if self.lastVal is not None and self.lastVal >= root.val:
            self.isBST = False
            return
        self.lastVal = root.val
        self.validate(root.right)
# 主函数
if __name__ == '__main__':
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(5)
    solution = Solution()
print("是否是BST：", solution.isValidBST(root))