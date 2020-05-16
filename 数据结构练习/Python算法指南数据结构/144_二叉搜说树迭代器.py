class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
class BSTIterator:
#参数root是二叉树的根节点
    def __init__(self, root):
        self.stack = []
        self.pos = root

    def hasNext1(self):
        return self.pos is not None or len(self.stack) > 0 # 只有栈为空和指针指向空节点才会返回False

    def next1(self):  # 非递归中序遍历的分解应用，调用一次该函数表示将求出一个中序后继
        while self.pos is not None:
            self.stack.append(self.pos)
            self.pos = self.pos.left
        self.pos = self.stack.pop()
        nxt = self.pos
        self.pos = self.pos.right
        return nxt


if __name__ == '__main__':
    root = TreeNode(10)
    root.left = TreeNode(1)
    root.right = TreeNode(11)
    root.left.right = TreeNode(6)
    root.right.right = TreeNode(12)
    iterator = BSTIterator(root)
    print("使用迭代器进行中序遍历的结果是：")
    while iterator.hasNext1():
        node = iterator.next1()
        print(node.val)