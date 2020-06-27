class Solution:
    def numSubmatrixSumTarget(self, matrix, target):
        row = len(matrix)
        col = len(matrix[0])
        prefixSum = [[0] * (col + 1) for _ in range(row + 1)]
        count = 0
        for i in range(1, row + 1):
            for j in range(1, col + 1):
                prefixSum[i][j] = prefixSum[i - 1][j] + prefixSum[i][j - 1] - prefixSum[i - 1][j - 1] + matrix[i - 1][j - 1]
                for x in range(i):
                    for y in range(j):
                        if prefixSum[i][j] - (prefixSum[i][y] + prefixSum[x][j]) + prefixSum[x][y] == target:
                            count += 1
        return count

if __name__ == "__main__":
    arr = [[1, 5, 7], [-13, 7, -8], [3, 3, -3], [4, -8, 9]]
    # 创建对象
    solution = Solution()
    print("输入的数组为：", arr)
    print("输出的结果是：", solution.submatrixSum(arr))
