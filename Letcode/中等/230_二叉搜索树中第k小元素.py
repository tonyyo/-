class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack, count = [], 0
        while root or stack:
            if root:  # 记得这里是root, 不是root.left
                stack.append(root)
                root = root.left
            else:
                pos = stack.pop()
                count += 1
                root = pos.right
                if count == k:
                    return pos.val
        return -1