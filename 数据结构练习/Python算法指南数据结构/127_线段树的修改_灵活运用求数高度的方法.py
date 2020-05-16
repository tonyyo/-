#树的定义
class TreeNode:
    def __init__(self, start, end, max):
        self.max = max
        self.start = start
        self.end = end
        self.left, self.right = None, None
class Solution:
#参数root、index、value是线段树的根，并使用[index, index]将节点的值更改为新的给定值
#返回列表
    def modify(self, root, index, value):
        pos = root
        if pos.start == index and pos.end == index: # 后续遍历途中进行值的修改，且因为修改的是叶子节点，所以要返回max
            pos.max = value
            return pos.max
        elif pos.left == None and pos.right ==None: # 这种要返回值的，不要遍历到空节点，遍历到叶子结点就好
            return pos.max
        leftMax = self.modify(pos.left, index, value)
        rightMax = self.modify(pos.right, index, value)
        pos.max = max(leftMax, rightMax)
        return pos.max

if __name__ == '__main__':
    #构建树
    root = TreeNode(1, 4, 3)
    root.left = TreeNode(1, 2, 2)
    root.right = TreeNode(3, 4, 3)
    root.left.left = TreeNode(1, 1, 2)
    root.left.right = TreeNode(2, 2, 1)
    root.right.left = TreeNode(3, 3, 0)
    root.right.right = TreeNode(4, 4, 3)
    solution = Solution()
    print("调用modify(root,2,4)")
    solution.modify(root, 2, 4)
    print([root.max, root.left.max, root.right.max, root.left.left.max, root.left.right.max, root.right.left.max,
           root.right.right.max])
    print("调用modify(root,4,0)")
    solution.modify(root, 4, 0)
    print([root.max, root.left.max, root.right.max, root.left.left.max, root.left.right.max, root.right.left.max,   root.right.right.max])