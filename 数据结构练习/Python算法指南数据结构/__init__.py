class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
class Solution:
    def max_high(self, root): # 求该树的最大高度
        if root is None:
            return 0
        left_length = self.max_high(root.left)
        right_length = self.max_high(root.right)
        return max(left_length, right_length) + 1

    def max_length(self, root):  # 前序遍历该树
        if root == None:
            return 0
        length = self.max_high(root.left) + self.max_high(root.right) + 1 # 左子树的高 + 右子树的高 + 1
        print(length)
        MAX1 = self.max_length(root.left)
        MAX2 = self.max_length(root.right)
        return max(length, MAX1, MAX2)

def printTree(root):
    import  collections
    queue = collections.deque()
    queue.append(root)
    ans = []
    while queue:
        pos = queue.popleft()
        ans.append(pos.val)
        if pos.left:
            queue.append(pos.left)
        if pos.right:
            queue.append(pos.right)
    print(ans)

if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print("原始二叉树为：")
    printTree(root)
    solution = Solution()
    print("最大长度为：")
    print(solution.max_length(root))