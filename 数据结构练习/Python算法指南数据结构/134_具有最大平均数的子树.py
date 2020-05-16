#树的定义
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
class Solution:
    def findSubtree2(self, root):
        result = []
        self.pre_order(root, result)
        return result[-1][0] # 返回最小平均值的树根节点

    def pre_order(self, root, result):
        if root is None:
            return
        self.temp = [0, 0] # 定义全局数组
        self.avgTree(root)
        sum = self.temp[0]
        size = self.temp[1]
        if len(result) == 0 or result[-1][1] < (sum/size):
            result.append([root, sum/size])
        self.pre_order(root.left, result)
        self.pre_order(root.right, result)

    def avgTree(self, root):  # 不能传递数字， 而应传递数组，因为数组存的是地址。
        if root is None:
            return
        self.temp[0] += root.val  # 利用全局变量记录和与节点的数量。
        self.temp[1] += 1
        self.avgTree(root.left)
        self.avgTree(root.right)


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
    root.right = TreeNode(11)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(-2)
    solution = Solution()
    print("给定二叉树是：", printTree(root))
    print("最大平均值的子树是：", printTree(solution.findSubtree2(root)))