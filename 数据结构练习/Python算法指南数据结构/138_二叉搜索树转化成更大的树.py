# 树的定义
#参数root是二叉树的根节点，类型是树节点
#返回值的类型是树节点，表示新的根
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
class Solution:
    def convertBST(self, root):
        self.sum = 0
        self.helper(root)
        return root
    def helper(self, root):
        if root is None:
            return
        self.helper(root.right) # 先访问右边
        self.sum += root.val
        root.val = self.sum
        self.helper(root.left)
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
    root = TreeNode(5)
    root.left = TreeNode(2)
    root.right = TreeNode(13)
    solution = Solution()
    print("原始二叉树为")
    printTree(root)
    root0 = solution.convertBST(root)
    print("转换后的树为")
    printTree(root0)