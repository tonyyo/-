import heapq

class Solution:
    def mergeNumber(self, numbers):
        heapq.heapify(numbers)  # 对numbers建堆
        sum = 0
        while len(numbers) != 1:
            a, b = heapq.heappop(numbers), heapq.heappop(numbers)  # 从堆中取最小值
            heapq.heappush(numbers, a + b)  # 将数加入堆
            sum += a + b
        return sum

if __name__ == '__main__':
    solution = Solution()
    list1 = [1,2,3,4]
    print(solution.mergeNumber(list1))
