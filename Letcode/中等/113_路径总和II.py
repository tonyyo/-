class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> [[int]]:
        if root == None:
            return []
        res = []
        self.f(root, sum, [], res)
        return res

    def f(self, root, sum, tmp, res):
        if root == None: # 可能存在单个不是叶子节点的情况
            return
        sum -= root.val  # 枚举回溯， sum不需要再加
        if root.left == None and root.right == None: # 这样才是叶子节点
            if sum == 0:
                res.append(tmp[:] + [root.val])
            return
        self.f(root.left, sum, tmp + [root.val], res)
        self.f(root.right, sum , tmp + [root.val], res)