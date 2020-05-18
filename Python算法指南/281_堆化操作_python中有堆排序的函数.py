import heapq
class Solution:
    def heapify(self, A):
        heapq.heapify(A)
if __name__ == '__main__':
    A = [3, 2, 1, 4, 5]
    print("输入的堆数组是：", A)
    solution = Solution()
    solution.heapify(A)
    print("堆化后的数组是：", A)