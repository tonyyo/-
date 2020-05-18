class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n // 2):
            for j in range((n + 1) // 2):   # 神来之笔，奇偶通吃
                temp = matrix[i][j]
                matrix[i][j] = matrix[n - 1 - j][i]   # 1
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j] # 4
                matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i] # 3
                matrix[j][n - 1 - i] = temp
if __name__ == '__main__':
    matrix = [
        [1, 2, 3],[4, 5, 6],[7, 8, 9]
    ]
    solution = Solution()
    solution.rotate(matrix)
    print(matrix)
