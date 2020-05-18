#树的定义
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
class Solution:
    def findSubtree(self, root):
        result = []
        self.pre_order(root, result)
        return result

    def pre_order(self, root, result):
        if root is None:
            return
        if len(result) == 0 or self.sumTree(root) < result[-1][1]: # 为空或者和更小时，追加到末尾
            result.append([root.val, self.sumTree(root)])
        self.pre_order(root.left, result)
        self.pre_order(root.right, result)

    def sumTree(self, root): # 求树的和
        if root is None:
            return 0
        leftSum = self.sumTree(root.left)
        rightSum = self.sumTree(root.right)
        return leftSum + rightSum + root.val # 以叶子节点为例，0 + 0 + 叶子值

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
    return (res)
#主函数
if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(-5)
    root.right = TreeNode(2)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(-4)
    root.right.right = TreeNode(-5)
    solution = Solution()
    print("最小子树的根节点是：", solution.findSubtree(root))