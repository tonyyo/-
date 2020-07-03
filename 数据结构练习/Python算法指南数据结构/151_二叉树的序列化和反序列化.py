#树的定义
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
class Solution:
    def serialize(self, root):
        if not root:
            return ['null'] # 遇到叶子结点，返回含null的列表即可
        ans = []            # 你也可以单独建全局列表，再分一个前序遍历函数
        ans.append(str(root.val))   # 前序遍历序列化
        ans += self.serialize(root.left) # 列表相连可以用加号
        ans += self.serialize(root.right)
        return ans

    def deserialize(self, data):  # 将data反序列化为树
        ch = data.pop(0)  # 根据前序遍历反序列化为树，这里的pop(0)用的很精髓
        if ch == 'null':
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