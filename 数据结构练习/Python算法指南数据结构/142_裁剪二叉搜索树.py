# 树的定义
#参数root是二叉搜索树的根节点
#参数minimum是最小的限制值
#参数maximum是最大的限制值
#返回值是新树的根节点
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
class Solution:
    def trimBST(self, root, minimum, maximum): # 返回符合条件的那颗树
        if not root:
            return None
        if root.val < minimum:   # 根节点值小于最小值，那么根节点以及左树都将小于，应该只往右走
            return self.trimBST(root.right, minimum, maximum)
        if root.val > maximum:   # 根节点值大于最大值，那么根节点和右树都将大于，应该只往左走
            return self.trimBST(root.left, minimum, maximum)
        root.left = self.trimBST(root.left, minimum, maximum)  # 根节点满足条件，继续遍历，左右都该走
        root.right = self.trimBST(root.right, minimum, maximum)
        return root

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
    root = TreeNode(8)
    root.left = TreeNode(3)
    root.right = TreeNode(10)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(6)
    root.right.right = TreeNode(14)
    root.left.right.left = TreeNode(4)
    root.left.right.right = TreeNode(7)
    root.right.right.left = TreeNode(13)
    solution = Solution()
    print("原始二叉树为")
    printTree(root)
    min = 5
    max = 13
    print("给定的max和min分别是", max, min)
    root0 = solution.trimBST(root, min, max)
    print("二分搜索树的结果是")
    printTree(root0)