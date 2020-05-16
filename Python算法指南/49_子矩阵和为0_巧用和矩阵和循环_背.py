class Solution:
    def submatrixSum(self, matrix):  # 该方法很巧妙, 但是只能找到一种
        row = len(matrix)
        col = len(matrix[0])
        prefixSum = [[0] * (col + 1) for _ in range(row + 1)]
        ans = []
        for i in range(1, row + 1):
            for j in range(1, col + 1):
                prefixSum[i][j] = prefixSum[i - 1][j] + prefixSum[i][j - 1] - prefixSum[i - 1][j - 1] + matrix[i - 1][
                    j - 1]
                for x in range(i):
                    for y in range(j):
                        if prefixSum[i][j] - (prefixSum[i][y] + prefixSum[x][j]) + prefixSum[x][y] == 0:
                            ans.append("" + str(x) + str(y) + str(i - 1) + str(j - 1))  # 存多种情况, 用字符串
        return ans

    def submatrixSum2(self, matrix):
        if not matrix:
            return []
        wide = len(matrix[0])
        depth = len(matrix)  # 这样表示二维列表的长度清晰可见
        res = None
        prefixsum = [[0 for j in range(wide + 1)] for i in range(depth + 1)]
        for dy in range(1, depth + 1):
            for dx in range(1, wide + 1):
                prefixsum[dy][dx] = prefixsum[dy - 1][dx] + prefixsum[dy][dx - 1] - prefixsum[dy - 1][dx - 1] + \
                                    matrix[dy - 1][dx - 1]  # 求和矩阵
                for y in range(dy):
                    for x in range(dx):
                        if prefixsum[dy][dx] == prefixsum[dy][x] + prefixsum[y][dx] - prefixsum[y][x]:  # 利用和矩阵求不同子矩阵的和
                            res = [(y, x), (dy - 1, dx - 1)]
                            return res


if __name__ == "__main__":
    arr = [[1, 5, 7], [-13, 7, -8], [3, 3, -3], [4, -8, 9]]
    # 创建对象
    solution = Solution()
    print("输入的数组为：", arr)
    print("输出的结果是：", solution.submatrixSum(arr))

# class Solution:
#     def submatrixSum(self, matrix):
#         if not matrix:
#             return []
#         wide = len(matrix[0])
#         depth = len(matrix) # 这样表示二维列表的长度清晰可见
#         res = None
#         prefixsum = [[0 for j in range(wide + 1)] for i in range(depth + 1)]
#         for dy in range(1, depth + 1):
#             for dx in range(1, wide + 1):
#                 prefixsum[dy][dx] = prefixsum[dy - 1][dx] + prefixsum[dy][dx - 1] - prefixsum[dy - 1][dx - 1] + \
#                                     matrix[dy - 1][dx - 1]  # 求和矩阵
#                 for y in range(dy):
#                     for x in range(dx):
#                         if prefixsum[dy][dx] == prefixsum[dy][x] + prefixsum[y][dx] - prefixsum[y][x]: # 利用和矩阵求不同子矩阵的和
#                             res = [(y, x), (dy - 1, dx - 1)]
#                             return res
