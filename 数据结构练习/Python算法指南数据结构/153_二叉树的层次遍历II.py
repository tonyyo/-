from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
class Solution:
    def levelOrderBottom(self, root):
        if root is None:
            return []
        queue = deque([root])
        result = []
        while queue:
            level = []
            size = len(queue)
            for _ in range(size):  # 这个是精髓
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return list(reversed(result))
# 主函数
if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    solution = Solution()
    print("层次遍历的结果是：", solution.levelOrderBottom(root))