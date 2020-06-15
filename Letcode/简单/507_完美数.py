class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        sum = 1
        if num <= 0:
            return False
        import math
        sqrt = math.sqrt(num)
        for i in range(2, math.ceil(sqrt)):
            if num % i == 0:
                sum += i
                sum += num // i
        if sqrt * sqrt == num:
            sum += sqrt
        return sum == num