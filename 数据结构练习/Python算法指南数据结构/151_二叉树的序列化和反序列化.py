#树的定义
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
class Solution:
    def serialize(self, root):
        if not root:
            return ['#'] # 遇到叶子结点，初始化列表
        ans = []
        ans.append(str(root.val))
        ans += self.serialize(root.left) # 列表相连可以用加号
        ans += self.serialize(root.right)
        return ans

    def deserialize(self, data):
        ch = data.pop(0)  # 根据列表建立树，该种情况只在该情况下可以构建树，不然的话需从中间开始，或者采用2 * n + 1/2 * n + 2。
        if ch == '#':
            return None
        else:
            root = TreeNode(int(ch))
        root.left = self.deserialize(data)
        root.right = self.deserialize(data)
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
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print("原始二叉树为：")
    printTree(root)
    solution = Solution()
    print("将二叉树序列化：")
    list0 = solution.serialize2(root)
    print(list0)
    print("将序列化的数字再次反序列化：")
    root0 = solution.deserialize2(list0)
    printTree(root0)