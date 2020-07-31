class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        x = y = pre = None # 两个交换的节点指针和前一个元素的指针
        stack = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                pos = stack.pop()
                if pre != None and pos.val < pre.val:
                    y = pos
                    if x == None:
                        x = pre
                pre = pos
                root = pos.right
        x.val, y.val = y.val, x.val