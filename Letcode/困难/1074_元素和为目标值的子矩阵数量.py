class Solution:
    def numSubmatrixSumTarget(self, matrix, target):
        row, col = len(matrix), len(matrix[0])
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