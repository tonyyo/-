# 树的定义
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
class Solution:
#参数root是一个给定的二叉搜索树
#参数target是一个给定的目标值
#返回值是二叉树中最接近target的值
    def closestValue(self, root, target):
        upper = root
        lower = root
        while root:
            if root.val > target:
                upper = root
                root = root.left
            elif root.val < target:
                lower = root
                root = root.right
            else:
                return root.val
        if abs(upper.val - target) > abs(lower.val - target):
            return lower.val
        return upper.val
def printTree(root):
    res = []
    if root is None:
        print(res)
    queue = []
    queue.append(root)
    while len(queue) != 0:
        tmp = []
        length = len(queue)
        for i in range(length):
            r = queue.pop(0)
            if r.left is not None:
                queue.append(r.left)
            if r.right is not None:
                queue.append(r.right)
            tmp.append(r.val)
        res.append(tmp)
    print(res)
if __name__ == '__main__':
    root = TreeNode(1)
    solution = Solution()
    print("原始二叉树为")
    printTree(root)
    target = 4.428571
    print("target=", target)
    root0 = solution.closestValue(root, target)
    print("最接近的target是：", root0)