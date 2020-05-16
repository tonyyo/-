#树的定义
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
class Solution:
#参数root是一个二叉树的根节点
#返回值是ArrayList中包含节点值的前序遍历
    def inorderTraversal(self, root):
        if root is None:
            return []
        return self.inorderTraversal(root.left) + [root.val] \
               + self.inorderTraversal(root.right)
# 主函数
if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    solution = Solution()
    print("树的中序遍历是：", solution.inorderTraversal(root))