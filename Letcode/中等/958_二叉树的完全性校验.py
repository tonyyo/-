class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        import collections
        queue = collections.deque()
        queue.append(root)
        flag = False # 是否出现过null节点
        while queue:
            level = []
            for _ in range(len(queue)):
                pos = queue.popleft()
                if flag and pos != None: # 前面出现空节点，但是弹出元素确是非空节点
                    return False
                if pos != None: # 不为空就有左节点和右节点，只不过可能为空而已
                    level.append(pos.left)
                    level.append(pos.right)
                else:
                    flag = True
            queue.extend(level)
        return True