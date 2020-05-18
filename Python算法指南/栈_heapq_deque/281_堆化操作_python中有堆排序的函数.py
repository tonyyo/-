import heapq
class Solution:
    def heapify(self, A):
        # heapq.heapify(A) # 对A直接建立了最小堆
        B = [-x for x in A] # 取相反数
        heapq.heapify(B)  # 对A的相反数建立最小堆，也就是对A建立最大堆
        C = [-x for x in B] # 取正后，获得最大堆
        return C
if __name__ == '__main__':
    A = [3, 2, 1, 4, 5]
    print("输入的堆数组是：", A)
    solution = Solution()
    print(solution.heapify(A))