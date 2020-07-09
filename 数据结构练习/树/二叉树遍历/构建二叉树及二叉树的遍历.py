import collections


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Tree(object):
    def buildTree(self, start, A):  # 从start处开始构造普通二叉树，一般从0开始
        if start >= len(A):
            return
        node = TreeNode(A[start])
        node.left = self.buildTree(2 * start + 1, A)  # 下一个节点为2 * start + 1
        node.right = self.buildTree(2 * start + 2, A)
        return node

    def BFS(self, root):
        result = []
        queue = collections.deque()
        queue.append(root)
        while queue:
            root = queue.popleft()
            result.append(root.val)
            if root.left is not None:
                queue.append(root.left)
            if root.right is not None:
                queue.append(root.right)
        return result

    def BFS2(root):
        res = []
        if root is None:
            print(res)
        queue = []
        queue.append(root)
        while len(queue) != 0:
            tmp = []
            length = len(queue)
            for i in range(length):
                r = queue.pop(0)
                tmp.append(r.val)
                if r.left is not None:
                    queue.append(r.left)
                if r.right is not None:
                    queue.append(r.right)
            res.append(tmp)
        print(res)

    def pre_order1(self, root, result):
        if root == None:
            return
        result.append(root.val)
        self.pre_order1(root.left, result)
        self.pre_order1(root.right, result)

    def pre_order2(self, root):
        result = []
        stack = []
        pos = root
        while pos is not None or stack:
            if pos is not None:
                result.append(pos.val)
                stack.append(pos)
                pos = pos.left
            else:
                pos = stack.pop()
                pos = pos.right
        return result

    def mid_order1(self, root, result):
        if root == None:
            return
        self.mid_order1(root.left, result)
        result.append(root.val)
        self.mid_order1(root.right, result)

    def mid_order2(self, root):
        result = []
        stack = []
        pos = root
        while pos is not None or stack:
            if pos is not None:
                stack.append(pos)
                pos = pos.left
            else:
                pos = stack.pop()
                result.append(pos.val)
                pos = pos.right
        return result

    def post_order1(self, root, result):
        if root == None:
            return
        self.post_order1(root.left, result)
        self.post_order1(root.right, result)
        result.append(root.val)

    def post_order2(self, root):
        stack1, stack2 = [], []
        stack1.append(root)
        while stack1:
            root = stack1.pop()
            stack2.append(root.val)
            if root.left:
                stack1.append(root.left)
            if root.right:
                stack1.append(root.right)
        return stack2[::-1] # 3 4 1 5 6 2 0

    def max_depth(self, root):
        if root == None:
            return 0
        ldepth = self.max_depth(root.left)
        rdepth = self.max_depth(root.right)

        return max(ldepth, rdepth) + 1

    def nums(self, root):
        if root == None:
            return 0

        lnums = self.nums(root.left)
        rnums = self.nums(root.right)

        return lnums + rnums + 1

if __name__ == '__main__':
    List = [1, 2, 3, 4, 5, 6, 7]
    solution = Tree()
    root = solution.buildTree(0, List)
    print(solution.BFS(root))
    print(solution.post_order2(root))
