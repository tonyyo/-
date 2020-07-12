class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def delete(self, root, val): # 删除以root为根节点的树中为val的节点, 并返回该树
        if root == None:
            return None
        if root.val > val:
            root.left = self.delete(root.left, val)
        if root.val < val:
            root.right = self.delete(root.right, val)
        if root.val == val:
            if root.left != None and root.right != None:
                maxVal = self.maxVal(root.left)
                root.val = maxVal
                root.left = self.delete(root.left, maxVal)   # 相当于将左右都不为空的子节点删除问题，转化为了删除左右子节点都为空的问题
            elif root.left == None and root.right == None:
                root = None
            elif root.left == None:
                root = root.right
            elif root.right == None:
                root = root.left
        return root

    def maxVal(self, root):
        if root.right == None:
            return root.val
        val = self.maxVal(root.right)
        return val

    def buildTree(self, A):  # 从start处开始构造普通二叉树，一般从0开始
        if len(A) == 1:
            return TreeNode(A[0])
        if len(A) == 0:
            return None
        mid = (len(A) - 1) // 2
        root = TreeNode(A[mid])
        root.left = self.buildTree(A[:mid])
        root.right = self.buildTree(A[mid + 1:])
        return root


    def bfs(self, root):
        import collections
        queue = collections.deque()
        queue.append(root)
        ans = []
        while queue:
            root = queue.popleft()
            ans.append(root.val)
            if root.left:
                queue.append(root.left)
            if root.right:
                queue.append(root.right)
        return ans

if __name__ == '__main__':
    solution = Solution()
    A = [1, 2, 3, 4, 5]
    root = solution.buildTree(A)
    print(solution.bfs(root))
    print(solution.bfs(solution.delete(root, 3)))