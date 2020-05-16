from collections import deque
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
class Solution:
    def levelOrder(self, root):
        if root is None:
            return []
        queue = deque([root])
        result = []
        while queue:
            level = [] # 记录一层的节点
            for _ in range(len(queue)): # 该层的个数由queue中的个数决定
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result

# 主函数
if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.left.left = TreeNode(8)
    root.left.right = TreeNode(21)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    solution = Solution()
    print("层序遍历的结果是：", solution.levelOrder(root))