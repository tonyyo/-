class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.sum = 0
        self.dfs(root, "")
        return self.sum
    def dfs(self, root, Str):
        if root == None:
            return
        Str += str(root.val)  # 注意 root不能为None
        if root.left == None and root.right == None:
            self.sum += int(Str)
            return
        self.dfs(root.left, Str)
        self.dfs(root.right, Str)

