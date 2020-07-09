# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: [int]) -> TreeNode:
        if len(nums) == 0:
            return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root

    def bfs(self, root):
        import collections
        queue = collections.deque()
        queue.append(root)
        result = []
        while queue:
            level = []
            for _ in range(len(queue)):
                pos = queue.popleft()
                level.append(pos.val)
                if pos.left:
                    queue.append(pos.left)
                if pos.right:
                    queue.append(pos.right)
            result.extend(level)
        return result

if __name__ == '__main__':
    nums = [-10,-3,0,5,9]
    solution = Solution()
    root = solution.sortedArrayToBST(nums)
    print(solution.bfs(root))