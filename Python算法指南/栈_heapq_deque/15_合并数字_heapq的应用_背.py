import heapq

class Solution:
    def mergeNumber(self, numbers):
        Q = []
        for i in range(len(numbers)):
            heapq.heappush(Q, numbers[i])
        ans = 0
        while len(Q) > 1:
            a = heapq.heappop(Q)
            b = heapq.heappop(Q)
            ans = ans + a + b
            heapq.heappush(Q, a + b)
        return ans

    def mergeNumber1(self, numbers):
        heapq.heapify(numbers)  # 对numbers建立最小堆
        result = 0
        while len(numbers) > 1:
            first = heapq.heappop(numbers) # 弹出numbers中最小值
            second = heapq.heappop(numbers)
            sum = first + second
            result += sum
            heapq.heappush(numbers, sum) # 往最小堆numbers中插入sum重新建堆
        return result

if __name__ == '__main__':
    solution = Solution()
    list1 = [1,2,3,4]
    print(solution.mergeNumber(list1))
    print(solution.mergeNumber1(list1))

# Q = []
# ans = 0
# for i in numbers:
#     heapq.heappush(Q, i)  # heapq是math中进行堆排序的模块, heappush是把元素加入堆中自动建堆, heappop是从堆中取出最小值
# while (len(Q) > 1):
#     a = heapq.heappop(Q)
#     b = heapq.heappop(Q)  # 这种方法特别适合用来取出最小的两个值, 进行操作
#     ans = ans + a + b
#     heapq.heappush(Q, a + b)  # 堆排序用来处理这种放回去重新排序的是神器
# return ans