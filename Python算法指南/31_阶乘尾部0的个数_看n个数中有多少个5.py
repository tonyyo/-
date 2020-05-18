class Solution:
    def trailingZeros(self, n): #求解整数阶乘尾部0的个数主要是算出有多少个5及其倍数，因为这些数与偶数相乘会产生0
        count = 0
        for i in range(5, n + 1):
            count += self.countFive(i)
        return count

    def countFive(self, n):
        count = 0
        while n % 5 == 0:  # 判断n中还有没有5, 而不是用n != 0
            n = n // 5
            count += 1
        return count

    def trailingZeros2(self, n):
        sum = 0
        while n != 0:
            n //= 5
            sum += n
        return sum
#主函数
if __name__ == '__main__':
    n = 100000
    print("初始值：", n)
    solution = Solution()
    print("结果：", solution.trailingZeros(n))
    print("结果：", solution.trailingZeros2(n))