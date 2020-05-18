class Solution:
    def Power(self, base, exponent):
        result = 1
        flag = 1 if exponent > 0 else -1
        exponent = exponent if flag == 1 else -exponent
        while exponent != 0:    # 把指数化成二进制，当指数中没有1的时候，结束循环
            if exponent & 1 == 1: # 举例:10^1101 = 10^0001*10^0100*10^1000。
                result *= base
            base = base * base
            exponent >>= 1   # 等价于 exponent //= 2
        return result if flag == 1 else 1 / result
if __name__ == '__main__':
    solution = Solution()
    print(solution.Power(2, -3))