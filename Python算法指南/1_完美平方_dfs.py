import math
class Solution:
    def numSquares(self, n):
        while n % 4 == 0:  # 去除4的倍数
            n //= 4
        if n % 8 == 7:
            return 4
        for i in range(int(n ** 0.5) + 1): # 保证本身可以取到
            temp = i * i
            temp2 = n - i * i
            if int(temp2 ** 0.5) ** 2 == temp2:  # 判断temp2是否是完全平方
                return 1 + (0 if temp == n or temp2 == n else 1) # 如果其中有一个正好等于n，那么就返回1，否则返回2
        return 3

if __name__ == '__main__':
    n = 1
    solution = Solution()
    print(solution.numSquares(n))
