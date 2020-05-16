import heapq
class Solution:
    def nthUglyNumber(self, n):
        heap = [1] #　最小丑数
        visited = set([1])  # 将列表转化为集合
        val = 0
        for _ in range(n):
            val = heapq.heappop(heap)  # 对heap列表建堆并弹出最小值
            for muti in [2, 3, 5]:
                result = val * muti
                if result not in visited:
                    visited.add(result)
                    heapq.heappush(heap, result)
        return val

if __name__ == '__main__':
    n = 3
    print("输入的n是：", n)
    solution = Solution()
    print("只含素因子2、3、5的第", n, "小的数是：", solution.nthUglyNumber(n))

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