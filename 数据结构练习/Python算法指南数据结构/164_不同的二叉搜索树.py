class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
class Solution:
    def generateTrees(self, n):
        return self.dfs(1, n)
    def dfs(self, start, end):
        if start > end: return [None]
        res = []
        for rootval in range(start, end + 1):
            LeftTree = self.dfs(start, rootval - 1)
            RightTree = self.dfs(rootval + 1, end)
            for i in LeftTree:
                for j in RightTree:
                    root = TreeNode(rootval)
                    root.left = i
                    root.right = j
                    res.append(root)
        return res
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
    n = int(input("请输入一个整数："))
    solution = Solution()
    list = solution.generateTrees(n)
    print("生成树的层次遍历分别是：")
    for i in list:
        print(printTree(i))