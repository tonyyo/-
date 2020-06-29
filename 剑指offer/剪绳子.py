class Solution:
    def cutRope(self, number):
        if number <= 3:
            return number
        a, b, c = 1, 2, 3 
        for i in range(4, number + 1):
            a, b, c = b, c, max(1 * c, 2 * b, 3 * a)
        return c

if __name__ == '__main__':
    solution = Solution()
    print solution.cutRope(8)
