class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
class Solution:
    def searchRange(self, root, k1, k2):
        ans = []
        if root is None:
            return ans
        queue = [root]
        index = 0
        while index < len(queue):
            if queue[index] is not None:
                if queue[index].val >= k1 and \
                                queue[index].val <= k2:
                    ans.append(queue[index].val)
                queue.append(queue[index].left)
                queue.append(queue[index].right)
            index += 1
        return sorted(ans)

    def searchRange2(self, root, k1, k2): # 返回一颗子树满足条件的数
        res = []
        if root is None:
            return []   # 完美利用局部列表完成任务
        res.extend(self.searchRange2(root.left, k1, k2))
        if k1 <= root.val <= k2:
            res.append(root.val)
        res.extend(self.searchRange2(root.right, k1, k2))
        return res


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
    root = TreeNode(20)
    root.left = TreeNode(8)
    root.right = TreeNode(22)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(12)
    print("原始二叉树是：")
    printTree(root)
    k1 = 10
    k2 = 22
    print("k1=", k1, "\nk2=", k2)
    solution = Solution()
    print("所有升序的节点值是：", solution.searchRange2(root, k1, k2))