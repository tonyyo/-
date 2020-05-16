class Solution:
    def kthSmallest(self, matrix, k):
        rowNum = len(matrix)
        colNum = len(matrix[0])
        merge = []
        for i in range(rowNum):
            for j in range(colNum):
                merge.append(matrix[i][j])
        merge = sorted(merge)  # sorted 函数有返回值 能对所有迭代对象进行排序,并且可以对字典的key进行排序
        print(merge)
        return merge[k - 1]
# 创建主函数
if __name__ == "__main__":
    arr = [[1, 5, 7], [3, 7, 8], [4, 8, 9]]
    index = 4
    # 创建对象
    solution = Solution()
    print("输入的数组是：", arr)
    print("运行后的结果是:", solution.kthSmallest(arr, index))

# class Solution:
#     def kthSmallest(self, matrix, k):
#         if not matrix or not matrix[0] or k == 0:
#             return None
#         while len(matrix) > 1:
#             matrix.append(self.merge(matrix.pop(0), matrix.pop(0)))   # 两个列表弹栈, 排序后, 存入栈, 再弹出两个栈, 进行排序, 直到全部排序.
#         return matrix[0][k - 1]
#     def merge(self, nums1, nums2):
#         res, index1, index2 = [], 0, 0
#         while index1 < len(nums1) or index2 < len(nums2):
#             if index1 >= len(nums1):
#                 res.append(nums2[index2])
#                 index2 += 1
#             elif index2 >= len(nums2):
#                 res.append(nums1[index1])
#                 index1 += 1
#             elif nums1[index1] < nums2[index2]:
#                 res.append(nums1[index1])
#                 index1 += 1
#             else:
#                 res.append(nums2[index2])
#                 index2 += 1
#         return res