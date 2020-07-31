class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    ans = 0  # 这种题目就是要定义一个全局变量
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if root == None:
            return 0
        self.f(root, sum)
        self.pathSum(root.left, sum)
        self.pathSum(root.right, sum)
        return self.ans

    def f(self, root, sum):
        if root == None:
            return
        sum -= root.val
        if sum == 0:
            self.ans += 1
        self.f(root.left, sum)
        self.f(root.right, sum)