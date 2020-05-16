# 树的定义
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
class Solution:
#参数root是一个二叉树的根节点
#返回值是一个整数
    def minDepth(self, root):
        return self.find(root)
    def find(self, node):
        if node is None:
            return 0
        left, right = 0, 0
        if node.left != None:
            left = self.find(node.left)
        else:
            return self.find(node.right) + 1
        if node.right != None:
            right = self.find(node.right)
        else:
            return left + 1
        return min(left, right) + 1
# 主函数
if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    solution = Solution()
    print("二叉树的最小深度是：", solution.minDepth(root))