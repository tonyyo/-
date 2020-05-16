#树的定义
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
class Solution:
#参数T1、T2是二叉树的根节点
#返回值是一个布尔值，当T2是T1的子树时返回True，否则返回False
    def pre_order(self, root, rt):
        if not root:
            return
        rt.append(root.val)
        self.pre_order(root.left, rt)
        self.pre_order(root.right, rt)

    def isSubtree(self, T1, T2):
        rt = []
        self.pre_order(T1, rt)
        string = "".join(str(x) for x in rt)
        rt2 = []
        self.pre_order(T2, rt2)
        string2 = "".join(str(x) for x in rt2)
        print(string)
        print(string2)
        return string.index(string2) != -1
#主函数
if __name__ == '__main__':
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.right.left = TreeNode(4)
    root2 = TreeNode(3)
    root2.right = TreeNode(4)
    solution = Solution()
    print("T2是否是T1的子树：", solution.isSubtree(root1, root2))