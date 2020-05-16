class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    ans = []  # 全局变量的使用

    def inorder(self, root, value):
        if root is None:
            return
        if root.val != value:
            self.ans.append(root.val) # 将非删除元素记录
        self.inorder(root.left, value)  # 调用成员变量或方法要用self
        self.inorder(root.right, value)

    def build(self, l, r):  # 利用二分法建立平衡二叉树
        if l == r:
            return TreeNode(self.ans[l])  # 建立叶子结点
        if l > r:
            return
        mid = (l + r) // 2
        node = TreeNode(self.ans[mid])  # 建立根节点和非叶子节点
        node.left = self.build(l, mid - 1)
        node.right = self.build(mid + 1, r)
        return node  # 返回一根子树

    def removeNode(self, root, value):
        self.inorder(root, value)
        self.ans = sorted(self.ans) # 建立平衡二叉树，首先得对数组排序
        return self.build(0, len(self.ans) - 1)
# 遍历这个树
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
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    solution = Solution()
    print("原来的二叉树是：", printTree(root))
    n = int(input("请输入要删除的节点值："))
    print("删除后的二叉树是：", printTree(solution.removeNode(root, n)))
