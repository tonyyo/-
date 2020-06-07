class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
class Solution():
    def buildTree(self, start, A):  # 从start处开始构造普通二叉树，一般从0开始
        if start >= len(A):
            return
        node = TreeNode(A[start])
        node.left = self.buildTree(2 * start + 1, A)  # 下一个节点为2 * start + 1
        node.right = self.buildTree(2 * start + 2, A)
        return node

    def preOrder(self, root):  # 跟层次遍历一样，每经历一次循环就弹出， 因为栈先进后出， 所以先将右子节点入栈
        res, stack = [], []
        stack.append(root)
        while stack:
            pos = stack.pop()
            res.append(pos.val)
            if pos.right:
                stack.append(pos.right)
            if pos.left:
                stack.append(pos.left)
        return res

    def inOrder(self, root):  # 一直向左，遇到一个左子节点为空，就弹出当前节点，然后往右， 若遇到空节点再次弹出
        res, stack = [], []
        cur = root
        while cur != None or stack:
            while cur != None:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res

    def postOrder1(self, root): # 前序遍历是中左右，后续遍历是左右中，反过来是中右左，那么只需调整前序遍历的代码，然后将结果逆序即可
        res, stack = [],[]
        stack.append(root)
        while stack:
            pos = stack.pop()
            res.append(pos.val)
            if pos.left:
                stack.append(pos.left)
            if pos.right:
                stack.append(pos.right)
        return res[::-1]

    def postOrder2(self, root):  # 类似中序遍历
        res, stack = [], []
        cur = root
        last = TreeNode(-1)
        while cur != None or stack:
            while cur != None:
                stack.append(cur)
                cur = cur.left
            cur = stack[-1]  # 获取栈顶节点
            if cur.right == None or cur.right == last: # 左右子节点为空时弹出，还有就是左右子节点上次访问过的弹出， 这就很抽象了
                res.append(cur.val)
                stack.pop()
                last = cur
                cur = None
            else:
                cur = cur.right
        return res


if __name__ == '__main__':
    solution = Solution()
    A = [1, 2, 3, 4, 5]
    root = solution.buildTree(0, A)
    print(solution.preOrder(root))
    print(solution.inOrder(root))
    print(solution.postOrder1(root))
    print(solution.postOrder2(root))
