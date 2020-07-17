class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def largestValues(self, root: TreeNode) -> [int]:
        if root == None:
            return []
        import collections
        queue, result = collections.deque(), []
        queue.append(root)
        while queue:
            level = []
            for _ in range(len(queue)):
                pos = queue.popleft()
                level.append(pos.val)
                if pos.left:
                    queue.append(pos.left)
                if pos.right:
                    queue.append(pos.right)
            result.append(max(level))
        return result
