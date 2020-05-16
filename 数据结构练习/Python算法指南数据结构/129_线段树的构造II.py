import collections


class SegmentTreeNode:
    def __init__(self, start, end):
        self.start, self.end = start, end
        self.left, self.right = None, None


class Solution:
    # 参数start、end表示段/区间
    # 返回线段树的根节点
    def build(self, start, end):
        if start > end:
            return None
        root = SegmentTreeNode(start, end)
        if start == end:
            return root
        root.left = self.build(start, (start + end) // 2)
        root.right = self.build((start + end) // 2 + 1, end)
        return root

    def build2(self, start, end):
        if start == end:
            return SegmentTreeNode(start, end) # 当不可再分，建立叶子节点
        node = SegmentTreeNode(start, end)
        node.left = self.build(start, (start + end) // 2)
        node.right = self.build((start + end) // 2 + 1, end)
        return node


def printTree(root):
    queue = collections.deque()
    queue.append(root)
    result = []
    while queue:
        pos = queue.popleft()
        result.append([pos.start, pos.end])
        if pos.left is not None:
            queue.append(pos.left)
        if pos.right is not None:
            queue.append(pos.right)
    return result

if __name__ == '__main__':
    solution = Solution()
    root = solution.build2(1, 6)
    print("构造的线段树是：")
    print(printTree(root))
