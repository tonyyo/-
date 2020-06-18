class Solution():
    def primeSelect(self, N):
        isPrime = [True for _ in range(N + 1)]
        prime = []
        for i in range(2, N + 1):
            if isPrime[i]:
                prime.append(i)
            for j in range(i * 2, N + 1, i):
                isPrime[j] = False
        return prime
if __name__ == '__main__':
    solution = Solution()
    print(solution.primeSelect(100))
