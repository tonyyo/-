import collections


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Tree(object):
    def __init__(self, root, List):
        queue = collections.deque()
        queue.append(root)
        List = List[::-1]
        while len(List) > 0:
            root = queue.popleft()
            treeNode = TreeNode(List.pop())
            root.left = treeNode
            queue.append(root.left)
            if len(List) > 0:
                treeNode2 = TreeNode(List.pop())
                root.right = treeNode2
                queue.append(root.right)

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
    root = TreeNode(0)
    tree = Tree(root, List)
    print(tree.BFS(root))