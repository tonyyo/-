#树的定义
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
class Solution:
#参数root是一个二叉树的根节点
#返回结果值
    def flatten(self, root):
        self.helper(root)
    #重组并按顺序返回最后一个节点
    def helper(self, root):
        if root is None:
            return None
        left_last = self.helper(root.left)
        right_last = self.helper(root.right)
        #连接
        if left_last is not None:
            left_last.right = root.right
            root.right = root.left
            root.left = None
        if right_last is not None:
            return right_last
        if left_last is not None:
            return left_last
        return root
#打印树函数
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
# 主函数
if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(6)
    solution = Solution()
    solution.flatten(root)
    print("变形后的结果是：", printTree(root))