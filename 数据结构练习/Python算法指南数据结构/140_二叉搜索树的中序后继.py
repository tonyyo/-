class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def inorderSuccessor(self, root, p):
        successor = None
        while root and root.val != p.val:
            if p.val < root.val:  #  // 只有往左查找时 successor 才需要不断更新
                successor = root
                root = root.left
            else:
                root = root.right
        return successor

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
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    solution = Solution()
    print("原始二叉树为")
    printTree(root)
    node = TreeNode(1)
    print("给定的节点是")
    printTree(node)
    root0 = solution.inorderSuccessor(root, node)
    print("该节点的后序遍历的后继是")
    print(root0.val)