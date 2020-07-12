class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
class Solution:
    def verticalOrder(self, root) -> [[int]]:
        from collections import deque, defaultdict
        if not root:
            return []
        queue = deque([(0, root)]) # 不仅存入节点，还存入数字，在一条垂直线上的数字相等
        lookup = defaultdict(list) # defaultdict(set),defaultdict(int)
        while queue:
            idx, node = queue.popleft()
            lookup[idx].append(node.val) # val是list类型，所有用append
            if node.left:
                queue.append((idx - 1, node.left))  # 往左减1
            if node.right:
                queue.append((idx + 1, node.right))  # 往右加1
        return [val for key, val in sorted(lookup.items(), key=lambda x : x[0])]

if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    solution = Solution()
    print("层次遍历的结果是：", solution.verticalOrder(root))