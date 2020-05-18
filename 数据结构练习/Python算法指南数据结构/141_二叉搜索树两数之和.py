class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
class Solution:
    def twoSum(self, root, n):
        if not root:
            return
        stack, check = [], set()
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val == n:
                return root.val
            elif n - root.val in check: # 在check中表示有这样的数
                return [root.val, n - root.val]
            if root.val not in check: # 存入check
                check.add(root.val)
            root = root.right
        return False


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
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    print("原始二叉树是：")
    printTree(root)
    n = 6
    solution = Solution()
    print("n=", n)
    print("在树中找到的和为n的两个数字是：", solution.findOne(root, n))