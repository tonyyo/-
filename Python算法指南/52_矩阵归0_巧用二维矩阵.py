class Solution:
    def setZeroes(self, matrix):
        if len(matrix) == 0:  # 当参数里面有矩阵时, 首先就要判断矩阵是否存在
            return
        width, depth = len(matrix[0]), len(matrix)
        row = [False for _ in range(depth)]  # 行标志列表
        col = [False for _ in range(width)]
        for i in range(depth):
            for j in range(width):
                if matrix[i][j] == 0:
                    row[i] = True
                    col[j] = True
        for i in range(depth):
            for j in range(width):
                if row[i] or col[j]:
                    matrix[i][j] = 0
        return matrix

#主函数
if __name__ == "__main__":
    arr = [[1, 2], [0, 3]]
    #创建对象
    solution = Solution()
    print("输入的数组是：", arr)
    print("变换后的矩阵是：", solution.setZeroes(arr))

# class Solution:
#     def setZeroes(self, matrix):
#         if len(matrix) == 0:
#             return
#         rownum = len(matrix)
#         colnum = len(matrix[0])
#         row = [False for i in range(rownum)]
#         col = [False for i in range(colnum)]
#         for i in range(rownum):
#             for j in range(colnum):
#                 if matrix[i][j] == 0:
#                     row[i] = True
#                     col[j] = True
#         for i in range(rownum):
#             for j in range(colnum):
#                 if row[i] or col[j]:  # 这样倒是很有意思
#                     matrix[i][j] = 0
#         return matrix