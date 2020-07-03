import collections


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def postorderTraversal(self, root):
        if root == None:
            return []
        stack1, stack = [], []
        stack1.append(root)
        while stack1:
            pos = stack1.pop()  # 就这个地方与层次遍历不同
            stack.append(pos.val)
            if pos.left:
                stack1.append(pos.left)
            if pos.right:
                stack1.append(pos.right)
        return stack[::-1] # 返回倒序

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
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print("原始二叉树为")
    printTree(root)
    solution = Solution()
    print("后序遍历的结果为", solution.postorderTraversal(root))
