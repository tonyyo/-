class Solution:
    def maximalRectangle(self, matrix):
        rowNum = len(matrix)
        colNum = len(matrix[0])
        newMatrix = [[0] * (colNum + 1) for _ in range(rowNum + 1)]  # 行多出第一行, 用来上下相加, 列多出一列, 用来以防序列是升序排列,栈无法弹出的情况
        for i in range(1, len(newMatrix)):
            for j in range(colNum):
                if matrix[i - 1][j] == 1: # 只有本身是1, 才能加上上一行的和
                    newMatrix[i][j] = newMatrix[i - 1][j] + matrix[i - 1][j]
        print(newMatrix)
        stack = []
        area = 0
        for i in range(1, len(newMatrix)):
            for j in range(len(newMatrix[0])):
                while stack and newMatrix[i][stack[-1]] > newMatrix[i][j]:
                    height_index = stack.pop()
                    height = newMatrix[i][height_index]
                    width = j - height_index
                    area = max(area, width * height)
                stack.append(j)
        return area
#主函数
if  __name__=="__main__":
    matrix=[[1,1,0,0,1],[0,1,0,0,1],[0,0,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]
    #创建对象
    solution=Solution()
    print("输入的布尔类型的二维矩阵是：",matrix)
    print("最大的矩阵的面积是：",solution.maximalRectangle(matrix))

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