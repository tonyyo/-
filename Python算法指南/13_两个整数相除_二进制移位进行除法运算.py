class Solutioin():
    def divide(self, dividend, divisor):
        shang = 0
        a, b = abs(dividend), abs(divisor)
        for i in range(32, -1, -1):  # 应该从大的倍数开始到小的倍数, 且可以为0, 表示不移动, 也就是倍数为1
            while a >= b << i:
                a -= b << i
                shang += 1 << i
        neg = ''
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            neg = '-'
        return neg + str(shang)

if __name__ == '__main__':
    solution = Solutioin()
    print(solution.divide(-90, 10))
