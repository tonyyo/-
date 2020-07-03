# 树的定义
# 参数root是一个树节点，表示二叉树的根节点
# 返回翻转后值
class invertBinaryTree:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    def invertTree(self, root):
        self.dfs(root)
        return root

    def dfs(self, node):  # 反转以node为根节点的二叉树
        if node == None:  # 如果node为None无需翻转
            return None
        left = node.left
        right = node.right
        node.left = right
        node.right = left
        if (left != None): self.dfs(left)
        if (right != None): self.dfs(right)


def printTree(root):
    if root == None:
        return
    printTree(root.left)
    print(root.val)
    printTree(root.right)

if __name__ == '__main__':
    root = invertBinaryTree(1)
    root.left = invertBinaryTree(2)
    root.right = invertBinaryTree(3)
    root.right.left = invertBinaryTree(4)
    print("原始二叉树为：")
    printTree(root)
    solution = Solution()
    solution.invertBinaryTree(root)
    print("翻转后的二叉树为：")
    printTree(root)
