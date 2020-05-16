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

    def kthPrime2(self, n):
        count = 0
        prime = [0] * (n + 1)

        for i in range(2, n):  #从4开始, 找出非质数, 剩下的就是质数
            for j in range(2 * i, n, i):
                prime[j] = 1

        for i in range(1, n):
            if prime[i] != 0:
                count += 1
        return count

    def kthPrime(self, n):
        visit = [0 for _ in range(n + 1)]
        for i in range(1, n + 1): # 从0到n的n个数
            if self.judgePrime(i): # 如果是质数就置1
                visit[i] = 1
        import collections
        result = collections.Counter(visit)
        return result[1]  # 返回1的个数


    def judgePrime(self, n):
        if n == 1:     # 1 不是质数
            return False
        if n == 2 or n == 3:  # 先把两种特殊情况搞定
            return True
        elif n % 6 != 1 and n % 6 != 5: # 该数不在6的两边, 一定不是质数
            return False
        import  math
        for i in range(2, int(math.sqrt(n))): # 就算该数在6的两边也不一定为质数
            if n % i == 0:
                return False
        return True
#主函数
if __name__ == '__main__':
    n = 13
    print("初始质数：", n)
    solution = Solution()
    print("结果：第{}个质数".format(solution.kthPrime(n)))