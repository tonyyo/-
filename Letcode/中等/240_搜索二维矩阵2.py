class Solution:
    def searchMatrix(self, matrix, target):
        M = len(matrix)
        if M == 0:
            return False
        N = len(matrix[0])
        if N == 0:
            return False
        x, y = 0, N - 1
        cur = matrix[x][y]
        while True:
            if cur < target:
                x += 1
            elif cur > target:
                y -= 1
            else:
                return True
            if  x >= M or y < 0:
                break
            cur = matrix[x][y]
        return False
if __name__ == '__main__':
    solution = Solution()
    matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    print(solution.searchMatrix(matrix, 5))
