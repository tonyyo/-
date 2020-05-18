class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
class Solution:
    def maxPathSum(self, root):
        self.maxSum = float('-inf')
        self._maxPathSum(root)
        return self.maxSum
    def _maxPathSum(self, root):
        if root is None:
            return 0
        left = self._maxPathSum(root.left)
        right = self._maxPathSum(root.right)
        left = left if left > 0 else 0
        right = right if right > 0 else 0
        self.maxSum = max(self.maxSum, root.val + left + right)
        return max(left, right) + root.val
# 主函数
if __name__ == '__main__':
    # 树的定义
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    solution = Solution()
    print("路径和最大为：", solution.maxPathSum(root))