class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
class Solution:
    def constructFromPrePost(self, preorder, inorder):  # 根据树的前序和中序序列建树
        if not inorder: # 当前序和中序遍历为空时，建立空树
            return None
        root = TreeNode(preorder[0])  # 建立根节点
        rootPos = inorder.index(preorder[0])  # 分割前序和中序序列的位置
        root.left = self.constructFromPrePost(preorder[1: 1 + rootPos], inorder[: rootPos])
        root.right = self.constructFromPrePost(preorder[rootPos + 1:], inorder[rootPos + 1:])
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
    preorder = [1, 2, 4, 5, 3, 6, 7]
    inorder = [4, 5, 2, 6, 7, 3, 1]
    print("前序遍历为：", preorder)
    print("中序遍历为：", inorder)
    solution = Solution()
    root = solution.constructFromPrePost(preorder, inorder)
    print("构造的二叉树为：")
    printTree(root)