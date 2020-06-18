class Solution():
    def isPrime(self, N):
        if N % 6 not in (1, 5) and N not in(2, 3):  # 2, 3是例外
            return False
        import math
        for i in range(3, int(math.sqrt(N) + 1)):
            if N != i and N % i == 0:
                return False
        return N != 1  # 1不是素数
if __name__ == '__main__':
    solution = Solution()
    print(solution.isPrime(4))
