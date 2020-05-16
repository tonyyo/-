#树的定义
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
class Solution:
#参数A是一个整数数组
#返回值是一个树节点
    def sortedArrayToBST(self, A):
        return self.convert(A, 0, len(A) - 1)
    def convert(self, A, start, end):
        if start > end:
            return None
        if start == end:
            return TreeNode(A[start])
        mid = (start + end) // 2
        root = TreeNode(A[mid])
        root.left = self.convert(A, start, mid - 1)
        root.right = self.convert(A, mid + 1, end)
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
    return (res)
# 主函数
if __name__ == '__main__':
    list = [1, 2, 3, 4, 5, 6, 7]
    print("列表为：", list)
    solution = Solution()
    print("排列完成的二叉树是：", printTree(solution.sortedArrayToBST(list)))