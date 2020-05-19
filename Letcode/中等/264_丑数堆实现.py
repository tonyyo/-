class Solution(object):
    def nthUglyNumber(self, n):
        result = []     # 存结果
        queue = []
        import heapq
        heapq.heappush(queue, 1)
        for i in range(n):
            min = heapq.heappop(queue)
            result.append(min)
            for x in [2, 3, 5]:
                if min * x not in queue:
                    heapq.heappush(queue, min * x)
        return result[n - 1]
if __name__ == '__main__':
    solution = Solution()
    print(solution.nthUglyNumber(10))
