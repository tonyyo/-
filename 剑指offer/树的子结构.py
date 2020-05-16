# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        if not pRoot2 or not pRoot1:
            return False
        flag = False
        flag = self.is_subTree(pRoot1, pRoot2)  # 前序遍历挨个判断子结构
        if flag == False:
            flag = self.HasSubtree(pRoot1.left, pRoot2)
        if flag == False:
            flag = self.HasSubtree(pRoot1.right, pRoot2)
        return flag

    def is_subTree(self, pRoot1, pRoot2):
        if pRoot1.val != pRoot2.val:
            return False
        if not pRoot2:  # 从树到了叶子节点
            if not pRoot1:
                return True # 主树也到了叶子结点，返回True
            else:
                return False
        if not pRoot1:   # 从树没到叶子结点，主树到了，返回False
            return False
        else:  # 当根节点相等时，比较子节点是否相等。
            return self.is_subTree(pRoot1.left, pRoot2.left) and self.is_subTree(pRoot1.right, pRoot2.right)

