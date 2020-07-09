class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.utils(root, None, None) # root不在任何树的左树和右树

    # 判断以root是否满足一棵二叉排序树的要求, minNode.val表示该节点如果处于右树下所不能小于的值，maxNode.val表示如果该节点处于左树下所不能大于的值。
    def utils(self, root, minNode, maxNode):
        if root == None: # 空树是一棵二叉排序树
            return True
        if minNode and root.val <= minNode.val: # 如果root在左树
            return False
        if maxNode and root.val >= maxNode.val:
            return False
        return self.utils(root.left, minNode, root) and self.utils(root.right, root, maxNode)
