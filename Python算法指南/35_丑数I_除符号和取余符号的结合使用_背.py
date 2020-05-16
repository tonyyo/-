class Solution:
    def isUgly(self, n):
        if n < 0:
            return False
        if n == 1:
            return True
        while n % 2 == 0: # 一直取余, 如果等于0, 说明还有该数的因子, 所以要整除掉它
            n //= 2
        while n % 3 == 0:
            n //= 3
        while n % 5 == 0:
            n //= 5
        return n == 1

# 主函数
if __name__ == '__main__':
    num = 14
    print("初始值：", num)
    solution = Solution()
    print("是否是丑数：", solution.isUgly(num))


class Solution:
    def isUgly(self, num):
        if num <= 0:
            return False
        if num == 1:  # 1也是丑数
            return True
        while num >= 2 and num % 2 == 0:
            num /= 2
        while num >= 3 and num % 3 == 0:
            num /= 3
        while num >= 5 and num % 5 == 0:
            num /= 5
        return num == 1
