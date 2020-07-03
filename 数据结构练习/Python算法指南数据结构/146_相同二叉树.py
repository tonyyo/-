class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
class Solution:
    def isSameTree(self, a, b):  # 比较两个树是否相等
        if a == None and b == None:
            return True
        if a == None or b == None:
            return False
        if a.val != b.val:
            return False
        a1 = self.isSameTree(a.left, b.left)
        b1 = self.isSameTree(a.right, b.right)
        return a1 and b1   # 节点相等，左树相等，右树相等，那么两棵树相等

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
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    print("原始二叉树1为")
    printTree(root1)
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    root2.left.right = TreeNode(4)
    print("原始二叉树2为")
    printTree(root2)
    solution = Solution()
    print("二叉树1与二叉树1进行判断：", solution.isIdentical(root1, root1))
    print("二叉树1与二叉树2进行判断：", solution.isIdentical(root1, root2))