class SegmentTreeNode:
    def __init__(self, start, end, max):
        self.start, self.end, self.max = start, end, max
        self.left, self.right = None, None


class Solution:
    # 参数A是一个整数数组
    # 返回值是线段树的根节点
    def build(self, A):
        return self.buildTree(0, len(A) - 1, A)

    def buildTree(self, start, end, A):  # 建立一颗三节点树
        if start == end:
            return SegmentTreeNode(start, end, A[start])
        node = SegmentTreeNode(start, end, 0)
        node.left = self.buildTree(start, (start + end) // 2, A)
        node.right = self.buildTree((start + end) // 2 + 1, end, A)
        node.max = max(node.left.max, node.right.max)
        return node

    def query(self, root, start, end): # 找该节点下存在于区间[start, end]的最大值
        if root.left == None and root.right == None:
            if end < root.start or start > root.end:
                return -65536  # 超出范围时返回一个超小值
            if start <= root.start and root.end <= end:
                return root.max
        leftMax = self.query(root.left, start, end)
        rightMax = self.query(root.right, start, end)
        return max(leftMax, rightMax)

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
            tmp.append(r.max)
        res.append(tmp)
    print(res)


if __name__ == '__main__':
    A = [1, 4, 2, 3]
    print("输入的数组是：", A)
    solution = Solution()
    root = solution.build(A)
    print("构造的线段树是：")
    printTree(root)
    print("运行query(root,1,1):", solution.query(root, 1, 1))
    print("运行query(root,1,2):", solution.query(root, 1, 2))
    print("运行query(root,2,3):", solution.query(root, 2, 3))
    print("运行query(root,0,2):", solution.query(root, 0, 2))
