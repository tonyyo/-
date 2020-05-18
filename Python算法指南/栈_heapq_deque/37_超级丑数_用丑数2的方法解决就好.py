import heapq
class Solution:
    def nthSuperUglyNumber(self, n, primes):
        minHeap = [1]
        heapq.heapify(minHeap)
        MIN = 0
        for i in range(n):
            MIN = heapq.heappop(minHeap) # 取n次最小值
            for x in primes:
                if MIN * x not in minHeap:  # 一定要去重，因为总会存在公倍数。
                    heapq.heappush(minHeap, MIN * x) # 建 len(minHeap) * n次堆
        return MIN
#主函数
if __name__ == '__main__':
    n = 6
    primes = [2, 7, 13, 19]
    print("初始值：", n)
    print("质数集合：", primes)
    solution = Solution()
    print("第{}个丑数：".format(n), solution.nthSuperUglyNumber(n, primes))