import math


class Solution:
    def reverse(self, x: int) -> int:
        listX = [v for v in str(x)]
        temp = ""
        if listX[0] == '-':
            temp = "-"
            listX = listX[1:]
        left, right = 0, len(listX) - 1
        while left < right:
            listX[left], listX[right] = listX[right], listX[left]
            left += 1
            right -= 1
        strX = "".join(listX)
        x = int(strX)
        res = int(temp + str(x))
        return res if -math.pow(2, 31) <= res <= math.pow(2, 31) - 1 else 0
if __name__ == '__main__':
    solution = Solution()
    print(solution.reverse(-120))