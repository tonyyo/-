class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
class Solution:
#参数root是一个二叉树的根节点
#返回值是今晚去打劫能够得到的最多金额
    def houseRobber3(self, root):
        rob, not_rob = self.visit(root)  # 对root节点是偷还是不偷
        return max(rob, not_rob)
    def visit2(self, root):
        if root is None:
            return 0, 0
        left_rob, left_not_rob = self.visit(root.left)
        right_rob, right_not_rob = self.visit(root.right)
        rob = root.val + left_not_rob + right_not_rob
        not_rob = max(left_rob, left_not_rob) + max(right_rob, right_not_rob)
        return rob, not_rob

    def visit(self, root):
        if root is None:  # 对象是否存在用none
            return 0, 0
        left_rob, left_not_rob = self.visit(root.left)
        right_rob, right_not_rob = self.visit(root.right)
        rob = root.val + left_not_rob + right_not_rob
        not_rob = max(left_not_rob, left_rob) + max(left_not_rob, right_rob)
        return rob, not_rob

#主函数
if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(1)
    solution = Solution()
    print("最多可以抢劫的金钱数是：", solution.houseRobber3(root))