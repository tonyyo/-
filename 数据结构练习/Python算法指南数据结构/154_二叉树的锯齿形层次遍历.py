class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
class Solution:
    def zigzagLevelOrder(self, root):
        if root is None:
            return []
        import collections
        queue, result = collections.deque(), []
        queue.append(root)
        count = 1
        while queue:
            level = []
            for _ in range(len(queue)):
                pos = queue.popleft()
                level.append(pos.val)
                if pos.left:
                    queue.append(pos.left)
                if pos.right:
                    queue.append(pos.right)
            if count % 2 == 1:  # 奇数层顺着遍历
                result.append(level)
            else:               # 偶数层反着遍历
                result.append(level[::-1])
            count += 1
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
    print("锯齿形层次遍历的结果是：", solution.zigzagLevelOrder(root))