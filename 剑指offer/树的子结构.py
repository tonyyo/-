# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSubStructure(self, pRoot1, pRoot2):    # pRoot2树是否是pRoot1树的子结构
        if not pRoot2 or not pRoot1:  # 空树不是任何树的子结构
            return False
        flag = self.is_subTree(pRoot1, pRoot2)  # 前序遍历挨个判断pRoot2树是否是pRoot1的子树的子结构
        if flag == False:
            flag = self.isSubStructure(pRoot1.left, pRoot2)
        if flag == False:
            flag = self.isSubStructure(pRoot1.right, pRoot2)
        return flag                             #  如果找到了就直接返回True， 无需继续判断

    def is_subTree(self, pRoot1, pRoot2):       # pRoot1和pRoot2的的根节点结构是否相等
        if not pRoot2:  # 从树到了叶子节点, 表明含子结构
            return True
        if not pRoot1:   # 从树没到叶子结点，主树到了，返回False
            return False
        if pRoot1.val != pRoot2.val:
            return False
        else:  # 当根节点相等时，比较子节点是否相等。
            return self.is_subTree(pRoot1.left, pRoot2.left) and self.is_subTree(pRoot1.right, pRoot2.right)

