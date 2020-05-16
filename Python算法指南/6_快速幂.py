class Solution:
    def fastPower(self, a, n, b): # 递归求快速幂，求a的n次幂
        if (n == 1):  # n等于1时，幂为a
            return a
        temp = self.fastPower(a, n // 2, b) % b
        return (1 if n % 2 == 0 else a) * temp * temp % 3 # 如果n是奇数，就会舍去一个a，所以要补上

if __name__ == '__main__':
    solution = Solution()
    print(solution.fastPower(2, 31, 3))