import heapq
class Solution:
    def nthSuperUglyNumber(self, n, primes):
        heap = [1]
        val = 0
        for _ in range(n):
            val = heapq.heappop(heap)
            for muti in primes:
                result = muti * val
                if result not in heap:
                    heapq.heappush(heap, result)
        return val
#主函数
if __name__ == '__main__':
    n = 6
    primes = [2, 7, 13, 19]
    print("初始值：", n)
    print("质数集合：", primes)
    solution = Solution()
    print("第{}个丑数：".format(n), solution.nthSuperUglyNumber(n, primes))