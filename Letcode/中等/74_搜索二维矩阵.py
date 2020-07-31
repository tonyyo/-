class Solution:
    def searchMatrix(self, matrix: [[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return  False
        left, right = 0, m * n - 1
        while left <= right: # 二分法找数应该在里面判断是否相等，出界条件为left > right
            mid = (left + right) // 2
            x = mid // n
            y = mid % n
            if target < matrix[x][y]:
                right = mid - 1
            elif target > matrix[x][y]:
                left = mid + 1
            else:
                return True
        return False
if __name__ == '__main__':
    matrix = [
      [1,   3,  5,  7],
      [10, 11, 16, 20],
      [23, 30, 34, 50]
    ]
    target = 3
    solution = Solution()
    print(solution.searchMatrix(matrix, target))