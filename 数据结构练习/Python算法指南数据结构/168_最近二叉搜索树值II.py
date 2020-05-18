#树的定义
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
class Solution:
#参数root是给定的二叉搜索树
#参数target是给定的目标值
#参数k是一个给定的k个值
#返回值是在二叉搜索树中最接近target的k个值
    def closestKValues(self, root, target, k):
        stack_upper = []
        stack_lower = []
        cur = root
        while cur:
            stack_upper.append(cur)
            cur = cur.left
        cur = root
        while cur:
            stack_lower.append(cur)
            cur = cur.right
        while len(stack_upper) > 0 and stack_upper[-1].val < target:
            self.move_upper(stack_upper)
        while len(stack_lower) > 0 and stack_lower[-1].val >= target:
            self.move_lower(stack_lower)
        ans = []
        for i in range(k):
            if len(stack_lower) == 0:
                upper = stack_upper[-1].val
                ans.append(upper)
                self.move_upper(stack_upper)
            elif len(stack_upper) == 0:
                lower = stack_lower[-1].val
                ans.append(lower)
                self.move_lower(stack_lower)
            else:
                upper, lower = stack_upper[-1].val, stack_lower[-1].val
                if upper - target < target - lower:
                    ans.append(upper)
                    self.move_upper(stack_upper)
                else:
                    ans.append(lower)
                    self.move_lower(stack_lower)
        return ans
    def move_upper(self, stack):
        cur = stack.pop()
        if cur.right:
            cur = cur.right
            while cur:
                stack.append(cur)
                cur = cur.left
    def move_lower(self, stack):
        cur = stack.pop()
        if cur.left:
            cur = cur.left
            while cur:
                stack.append(cur)
                cur = cur.right
def printTree(root):
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
            if r.left is not None:
                queue.append(r.left)
            if r.right is not None:
                queue.append(r.right)
            tmp.append(r.val)
        res.append(tmp)
    print(res)
if __name__ == '__main__':
    root = TreeNode(1)
    solution = Solution()
    print("原始二叉树为")
    printTree(root)
    target = 0.000000
    k = 1
    print("target=", target, "\nk=", k)
    root0 = solution.closestKValues(root, target, k)
    print("最接近的target是：", root0)