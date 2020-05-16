class Solution:
    def searchMatrix(self, matrix, target):
        width, depth = len(matrix[0]), len(matrix)
        x = 0
        y = width - 1
        flag = False
        while x >= 0 and y < depth:  # 不规则循环用while, 因为用用for不好判断循环继续条件
            if matrix[x][y] > target:
                x += 1
            elif matrix[x][y] < target:
                y -= 1
            else:
                flag = True
        return flag
# 主函数
if __name__ == "__main__":
    arr = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
    target = 3
    # 创建对象
    solution = Solution()
    print("输入的整数数组是：", arr)
    print("输入的目标值是", target)
    print("输出的结果是：", solution.searchMatrix(arr, target))

# class Solution:
#     def searchMatrix(self, matrix, target):
#         if matrix == None or len(matrix) == 0:
#             return False
#         depth, width = len(matrix), len(matrix[0])
#         x, y = 0, width - 1   # 从每一行的最后一个数开始比较, 如果小于target, 向前移动, 如果大于target, 则从下一行的最后一个数开始比较
#         while x <= depth - 1 and y >= 0:
#             goal = matrix[x][y]
#             if target > goal:
#                 x += 1
#             if target < goal:
#                 y -= 1
#             if target == goal:
#                 return True
#         return False