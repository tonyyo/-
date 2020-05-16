class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
class Solution:
#参数root是一个二叉树的根节点
#返回值是ArrayList中包含节点值的前序遍历
    def preorderTraversal(self, root):
        self.results = []
        self.traverse(root)
        return self.results
    def traverse(self, root):
        if root is None:
            return
        self.results.append(root.val)
        self.traverse(root.left)
        self.traverse(root.right)
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
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print("要遍历的树是：", printTree(root))
    solution = Solution()
    print("前序遍历的结果是：", solution.preorderTraversal(root))