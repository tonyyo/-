class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def constructFromPrePost(self, pre: [int], post: [int]):
        if len(pre) == 0:
            return None
        if len(pre) == 1:    # 这里为1时要返回，不然下面的pre[1]会报错
            return TreeNode(pre[0])
        midPos = 0
        for i in range(len(pre)):
            if post[i] == pre[1]:
                midPos = i + 1  # 前序遍历的第一个节点是后续遍历的最后一个节点
                break
        root = TreeNode(pre[0])
        root.left = self.constructFromPrePost(pre[1 : midPos + 1], post[: midPos])
        root.right = self.constructFromPrePost(pre[midPos + 1 :], post[midPos : -1])
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
