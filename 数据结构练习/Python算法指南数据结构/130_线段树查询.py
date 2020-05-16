#线段树的定义
class SegmentTreeNode:
    def __init__(self, start, end, count):
        self.start, self.end, self.count = start, end, count
        self.left, self.right = None, None
class Solution:
#参数root、start、end是线段树的根节点，一个段和间隔
#返回值是间隔[start, end]中计数的元素个数
    def query(self, root, start, end):
        if root is None:
            return 0
        if root.start > end or root.end < start:
            return 0
        if start <= root.start and root.end <= end:
            return root.count
        return self.query(root.left, start, end) + self.query(root.right, start, end)

    def query2(self, root, start, end): # 节点root下[start, end]的元素个数
        # if start > root.end or end < root.start:  其实该行代替下行更好，想想为什么
        if root.left == None and root.right == None and start > root.end or end < root.start:
            return 0  # 当叶子节点不满足范围时，返回0就好
        if root.left == None and root.right == None and start <= root.start and root.end <= end:
            return root.count
        left_count = self.query2(root.left, start, end)
        right_count = self.query2(root.right, start, end)
        return left_count + right_count

#主函数
if __name__ == '__main__':
    root = SegmentTreeNode(0, 3, 3)
    root.left = SegmentTreeNode(0, 1, 1)
    root.right = SegmentTreeNode(2, 3, 2)
    root.left.left = SegmentTreeNode(0, 0, 1)
    root.left.right = SegmentTreeNode(1, 1, 0)
    root.right.left = SegmentTreeNode(2, 2, 1)
    root.right.right = SegmentTreeNode(3, 3, 1)
    solution = Solution()
    print("对于数组[0,null,2,3]的线段树，查询为（1,1）的结果是：", solution.query2(root, 1, 2))