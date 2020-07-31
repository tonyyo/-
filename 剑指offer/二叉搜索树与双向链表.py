class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    head, tail, pre = None, None, None
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if root == None:
            return None
        self.inorder(root)
        self.head.left = self.tail
        self.tail.right = self.head
        return self.head

    def inorder(self, root):
        if root == None:
            return
        self.inorder(root.left)
        if self.pre == None: # 无前驱节点，表明为第一个元素
            self.head = root
        else:
            self.pre.right = root
        root.left = self.pre
        self.pre = root
        self.tail = root
        self.inorder(root.right)

