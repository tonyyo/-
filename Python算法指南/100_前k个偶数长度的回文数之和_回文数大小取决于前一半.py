class Solution:
    def sumKEven(self, k):
        total = 0
        for number in range(1, k + 1):
            total += self.makePalindromeNumber(number)
        return total
    def makePalindromeNumber(self, number):
        number_s = str(number)
        number_s = number_s + number_s[::-1]    # 回文数的大小其实取决的是前一半的大小
        return int(number_s)
if __name__ == '__main__':
    k = 10
    print("初始值：", k)
    solution = Solution()
    print("结果：", solution.sumKEven(k))