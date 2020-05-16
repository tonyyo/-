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
        if root.val < minimum:
            return self.trimBST(root.right, minimum, maximum)
        if root.val > maximum:
            return self.trimBST(root.left, minimum, maximum)
        root.left = self.trimBST(root.left, minimum, maximum)
        root.right = self.trimBST(root.right, minimum, maximum)
        return root

    def trimBST2(self, root, mininum, maximum):  # 对一颗一颗子树进行裁剪， 然后返回。
        if root is None:
            return
        if root.val > maximum: # 当根节点值比最大值大，返回裁剪好的左子树。
            return self.trimBST2(root.left, mininum, maximum)
        if root.val < mininum:
            return self.trimBST2(root.right, mininum, maximum)
        root.left = self.trimBST2(root.left, mininum, maximum)
        root.right = self.trimBST2(root.right, mininum, maximum)
        return root # 当在区间内时， 返回一颗完全的数。

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
    root0 = solution.trimBST2(root, min, max)
    print("二分搜索树的结果是")
    printTree(root0)