# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> [int]:
        if root == None:
            return []
        import collections
        queue, result = collections.deque(), list()
        queue.append(root)
        while queue:
            level = list()
            for _ in range(len(queue)):
                pos = queue.popleft()
                level.append(pos)
                if pos and pos.left != None:
                    queue.append(pos.left)
                if pos and pos.right != None:
                    queue.append(pos.right)
            if len(level) != 0:
                result.append(level[-1].val)
        return result