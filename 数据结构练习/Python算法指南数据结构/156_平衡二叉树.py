class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
class Solution:
    def isBalanced(self, root):
        balanced, _ = self.validate(root)
        return balanced
    def validate(self, root):
        if root is None:
            return True, 0
        balanced, leftHeight = self.validate(root.left)
        if not balanced:
            return False, 0
        balanced, rightHeight = self.validate(root.right)
        if not balanced:
            return False, 0
        return abs(leftHeight - rightHeight) <= 1, max(leftHeight, rightHeight) + 1
# 主函数
if __name__ == '__main__':
    #树A
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    # 树B
    root1 = TreeNode(3)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    solution = Solution()
    print("树A是否平衡：", solution.isBalanced(root))
    print("树B是否平衡：", solution.isBalanced(root1))