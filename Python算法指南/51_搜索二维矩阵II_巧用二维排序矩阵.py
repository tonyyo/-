class Solution:
    def searchMatrix(self, matrix, target):
        if matrix == [] or matrix[0] == []:
            return 0
        row, column = len(matrix), len(matrix[0])
        i, j = row - 1, 0   # 从左下角的位置开始索引
        count = 0
        while i >= 0 and j < column:
            if matrix[i][j] == target:  # 因为往别的地方都行不通了, 所以要往右上方向移动.
                count += 1
                i -= 1
                j += 1
            elif matrix[i][j] < target: # 如果target较大, 则往右搜索更大的
                j += 1
            elif matrix[i][j] > target:  # 如果target较小, 则往上搜索更小的
                i -= 1
        return count
# 主函数
if __name__ == "__main__":
    arr = [[1, 3, 5, 7], [2, 4, 7, 8], [3, 5, 9, 10]]
    target = 3
    # 创建对象
    solution = Solution()
    print("输入的数组是：", arr)
    print("输入的目标值是：", target)
    print("该目标出现的次数是：", solution.searchMatrix(arr, target))