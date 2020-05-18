class Solution:
    def maximalRectangle2(self, matrix):
        rowNum, colNum = len(matrix), len(matrix[0])
        for i in range(1, rowNum):  # 从第二行开始
            for j in range(colNum):
                if matrix[i][j] == 1:
                    matrix[i][j] = matrix[i - 1][j] + 1
        area = 0
        for i in range(rowNum):
            area = max(area, self.maxAreaOfRow(matrix[i])) # 前n行的最大直方图面积
        return area

    def maxAreaOfRow(self, A):
        stack, area = [], 0
        A.append(0) # 栈的末尾是最小的元素，所以会弹出所有高的索引
        for i in range(len(A)):
            while stack and A[stack[-1]] > A[i]:
                higthest_index = stack.pop()
                higthest = A[higthest_index]
                width = i - higthest_index
                area = max(area, higthest * width)
            stack.append(i)
        return area
#主函数
if  __name__=="__main__":
    matrix=[[1,1,0,0,1],[0,1,0,0,1],[0,0,1,1,1],[0,0,1,1,1],[0,0,0,0,1]]
    #创建对象
    solution=Solution()
    print("输入的布尔类型的二维矩阵是：",matrix)
    print("最大的矩阵的面积是：",solution.maximalRectangle(matrix))
    print("最大的矩阵的面积是：",solution.maximalRectangle2(matrix))

# class Solution:
#     def maximalRectangle(self, matrix):
#         if not matrix:
#             return 0
#         max_rectangle = 0
#         heights = [0] * len(matrix[0]) # 建立一个以matrix宽为长度的列表
#         for row in matrix:  # 这样表示取matirx的一个元素, 也就是一个列表.
#             for index, num in enumerate(row):
#                 heights[index] = heights[index] + 1 if num else 0
#             max_rectangle = max(
#                 max_rectangle,
#                 self.find_max_rectangle(heights),
#             )
#         return max_rectangle
#     def find_max_rectangle(self, heights):
#         indices_stack = []
#         max_rectangle = 0
#         for index, height in enumerate(heights + [-1]):
#             while indices_stack and heights[indices_stack[-1]] >= height:
#                 popped = indices_stack.pop(-1)
#                 left_bound = indices_stack[-1] if indices_stack else -1
#                 max_rectangle = max(
#                     max_rectangle,
#                     (index - left_bound - 1) * heights[popped],
#                 )
#             indices_stack.append(index)
#             # print(indices_stack)
#         return max_rectangle