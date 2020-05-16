class Solution:
    def isPerfectSquare2(self, n):
        return int((n ** 0.5) ** 2) == n

if __name__ == '__main__':
    solution = Solution()
    print(solution.isPerfectSquare2(9))

