class Solution:
    def kthPrime1(self, n):
        prime = [0] * 100009
        for i in range(2, n):
            if prime[i] == 0:
                for j in range(2 * i, n, i):
                    prime[j] = 1
        ans = 1
        for i in range(2, n):
            if prime[i] == 0:
                ans += 1
        return ans

    def kthPrime(self, n):
        count = 0
        prime = [0] * (n + 1)

        for i in range(2, n):  #从4开始, 找出非质数, 剩下的就是质数
            for j in range(2 * i, n, i):
                prime[j] = 1

        for i in range(1, n):
            if prime[i] != 0:
                count += 1
        return count
#主函数
if __name__ == '__main__':
    n = 13
    print("初始质数：", n)
    solution = Solution()
    print("结果：第{}个质数".format(solution.kthPrime(n)))