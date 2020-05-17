class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    diam = 0

    def diameterOfBinaryTree(self, root):
        self.dfs(root)
        return self.diam

    def dfs(self, root): # 返回子节点的最大深度
        if root == None:
            return 0
        leftDept = self.dfs(root.left)
        rightDept = self.dfs(root.right)
        dept = 1 + max(leftDept, rightDept)
        self.diam = max(self.diam, leftDept + rightDept)
        return dept

if __name__ == '__main__':
    solution = Solution()
    print(solution.diameterOfBinaryTree())