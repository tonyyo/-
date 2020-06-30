import heapq
class Solution:
    def nthUglyNumber(self, n, a, b, c):
        heap = [1] #　最小丑数
        val = 0
        for _ in range(n + 1):
            val = heapq.heappop(heap)  # 对heap列表建堆并弹出最小值
            print(val, end=" ")
            for muti in [a, b, c]:
                result = val * muti
                if result not in heap:
                    heapq.heappush(heap, result)
        return val

if __name__ == '__main__':
    solution = Solution()
    print(solution.nthUglyNumber(5, 2, 11, 13))

# class Solution:
#     def nthUglyNumber(self, n):
#         heap = [1]  #初始堆, 里面有一个最小丑数1
#         visited = set([1])  # 存储丑数, 用set存储, 防止重复
#         val = None  # 存储第n小的数, 可以用None初始化
#         for i in range(n):          # heapq讲解:https://www.jianshu.com/p/801318c77ab5
#             val = heapq.heappop(heap)  # 每次取出最小值, 取了三次, 最后一次取值就是第n小的值
#             for multi in [2, 3, 5]:   #直接用2,3,5中的值反复相乘, 得到的就是丑数
#                 if val * multi not in visited:
#                     visited.add(val * multi)
#                     heapq.heappush(heap, val * multi)
#         return val