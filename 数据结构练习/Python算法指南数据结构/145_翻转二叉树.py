# 树的定义
# 参数root是一个树节点，表示二叉树的根节点
# 返回翻转后值
class invertBinaryTree:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    def invertBinaryTree(self, root):
        self.dfs1(root)

    def dfs(self, node):
        left = node.left
        right = node.right
        node.left = right
        node.right = left
        if (left != None): self.dfs(left)
        if (right != None): self.dfs(right)

    def dfs1(self, node):
        if node == None:
            return
        left = self.dfs1(node.left)  # 必须赋临时值，不然会左子树会覆盖右子树
        right = self.dfs1(node.right)
        node.left = right
        node.right = left
        return node


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
