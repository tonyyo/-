class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
class Solution:
    def verticalOrder(self, root) -> [[int]]:
        from collections import defaultdict, deque
        if not root:
            return []
        queue = deque([(0, root)]) # 不仅存入节点，还存入数字，在一条垂直线上的数字相等
        lookup = list()
        while queue:
            level = list()
            for _ in range(len(queue)):
                idx, node = queue.popleft()
                level.append([idx, node.val])
                if node.left:
                    queue.append((idx - 1, node.left))  # 往左减1
                if node.right:
                    queue.append((idx + 1, node.right))  # 往右加1
            lookup.extend(level)
        print(lookup)
        return [val for idx, val, in sorted(lookup, key=lambda x: x[0])] #
if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    solution = Solution()
    print("层次遍历的结果是：", solution.verticalOrder(root))