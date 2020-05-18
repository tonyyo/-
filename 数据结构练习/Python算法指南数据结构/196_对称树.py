class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
class Solution:
    def check_symmetry(self, nodeA, nodeB):
        if nodeA is None and nodeB is None:
            return True
        if nodeA is None or nodeB is None:
            return False
        if nodeA.val != nodeB.val:
            return False
        outer_result = self.check_symmetry(nodeA.left, nodeB.right)
        inner_result = self.check_symmetry(nodeA.right, nodeB.left)
        return outer_result and inner_result
    def isSymmetric(self, root):
        if root is None:
            return True
        return self.check_symmetry(root.left, root.right)
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
#主函数
if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)
    solution = Solution()
    printTree(root)
    print("是否是对称的：", solution.isSymmetric(root))
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(3)
    printTree(root)
    print("是否是对称的：", solution.isSymmetric(root))