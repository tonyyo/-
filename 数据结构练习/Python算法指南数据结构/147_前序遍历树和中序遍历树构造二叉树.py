class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
class Solution:
    def buildTree(self, preorder, inorder):
        if not inorder: return None  # i
        root = TreeNode(preorder[0])
        rootPos = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1: 1 + rootPos], inorder[: rootPos])
        root.right = self.buildTree(preorder[rootPos + 1:], inorder[rootPos + 1:])
        return root

    def buildTree1(self, pre, tin): # 根据前序和后序序列构造二叉树
        if len(tin) <= 0:
            return None
        root = TreeNode(pre[0])
        pos = tin.index(pre[0])
        root.left = self.buildTree1(pre[1:pos + 1], tin[:pos])
        root.right = self.buildTree1(pre[pos + 1:], tin[pos + 1:])
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
    print(res)
if __name__ == '__main__':
    inorder = [1, 2, 3]
    preorder = [2, 1, 3]
    print("前序遍历为：", preorder)
    print("中序遍历为：", inorder)
    solution = Solution()
    root = solution.buildTree1(preorder, inorder)
    print("构造的二叉树为：")
    printTree(root)