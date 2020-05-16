class Solution:
    def submatrixSum2(self, matrix):
        rowNum, colNum = len(matrix), len(matrix[0])
        Sum = [[0 for _ in range(colNum + 1)] for _ in range(rowNum + 1)]
        result = []
        for i in range(rowNum):
            for j in range(colNum):
                Sum[i][j] = Sum[i - 1][j] + Sum[i][j - 1] - Sum[i - 1][j - 1] + matrix[i][j]
                for k in range(i):  # 按理来说应该先求出和，再来求子矩阵和，但是为了节省时间复杂度，采用了该技巧
                    for l in range(j):
                        if Sum[i][j] - Sum[k - 1][j] - Sum[i][l - 1] + Sum[k - 1][l - 1] == 0:
                            result.append([(k, l), (i, j)])
        return result

if __name__ == "__main__":
    arr = [[1, 5, 7], [-13, 7, -8], [3, 3, -3], [4, -8, 9]]
    # 创建对象
    solution = Solution()
    print("输入的数组为：", arr)
    print("输出的结果是：", solution.submatrixSum2(arr))
    print("输出的结果是：", solution.submatrixSum(arr))
