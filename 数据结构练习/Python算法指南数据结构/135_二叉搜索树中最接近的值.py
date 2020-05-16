class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
class Solution:
    def closestKValues(self, root, target, k):
        self.allNodes = []
        self.pre_order(root, target)
        self.allNodes = sorted(self.allNodes, key = lambda x : x[0]) # 按差值排序
        result = []
        for i in range(k):
            result.append(self.allNodes[i][1]) # 记录k个最接近的值
        return result

    def pre_order(self, root, target):
        if root is None:
            return
        self.allNodes.append([abs(root.val - target), root.val]) # 记录差值和节点值
        self.pre_order(root.left, target)
        self.pre_order(root.right, target)
#主函数
if __name__=="__main__":
    root=TreeNode(1)
    target = 0.000000
    k = 1
    #创建对象
    solution=Solution()
    print("root=",root,"target=",target,"k=",k)
    print("输出的结果是：",solution.closestKValues(root,target,k))