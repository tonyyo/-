class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
class Solution:
    def insertNode(self, root, node):
        if root is None:
            return node
        curt = root
        while curt != node:
            if node.val < curt.val:
                if curt.left is None:
                    curt.left = node
                curt = curt.left
            else:
                if curt.right is None:
                    curt.right = node
                curt = curt.right
        return root

    def insertNode2(self, root, node):
        cur = root # 从根节点开始查找
        while True: # 等到指针指向插入节点为止
            if cur.val > node.val: # 当前值大于节点值往左
                if cur.left == None:  # 如果左边是空，直接插入
                    cur.left = node
                    break  # 插入后，就跳出循环就好
                cur = cur.left
            else:
                if cur.right == None:
                    cur.right = node
                    break
                cur = cur.right
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
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(3)
    solution = Solution()
    node = TreeNode(0)
    print("原始二叉树为")
    printTree(root)
    print("插入节点为：")
    printTree(node)
    root0 = solution.insertNode2(root, node)
    print("插入后的树为")
    printTree(root0)