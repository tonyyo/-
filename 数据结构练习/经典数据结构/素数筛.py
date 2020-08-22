class Solution():
    def primeSelect(self, N, num):
        isPrime = [True] * (N + 1)
        isPrime[0], isPrime[1] = False, False
        for i in range(2, N + 1):
            for j in range(2 * i, N + 1, i): # 从2的2倍数开始筛
                isPrime[j] = False
        return isPrime[num]

if __name__ == '__main__':
    solution = Solution()
    print(solution.primeSelect(100, 8))
