#树的定义
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
class Solution(object):
    def countNodes(self, root):
#root的类型是树节点
#返回值的类型是整数型
#一直向左下走来计算深度
        def getDepth(Node):
            if Node == None:
                return 0
            depth = 1
            while Node.left != None:
                depth += 1
                Node = Node.left
            return depth
        if root == None:
            return 0
        rightT = root.right
        leftT = root.left
        rDepth = getDepth(rightT)
        lDepth = getDepth(leftT)
        #如果左右子树深度相同，那么说明右子数是满二叉树，左子树是完全二叉树
        if rDepth == lDepth:
            return self.countNodes(rightT) + 2 ** lDepth
        #否则说明左子树是满二叉树，右子树是完全二叉树
        else:
            return self.countNodes(leftT) + 2 ** rDepth

    def countNodes2(self, root):
        if root == None:
            return 0
        left = self.countNodes(root.left)
        right = self.countNodes(root.right)
        return left + right + 1

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
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    solution = Solution()
    print("原始二叉树为")
    printTree(root)
    total = solution.countNodes2(root)
    print("完全树节点数是：", total)