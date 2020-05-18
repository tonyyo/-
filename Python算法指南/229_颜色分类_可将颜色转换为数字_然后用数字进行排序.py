class Solution:
    def sortColors(self, A):
        left, index, right = 0, 0, len(A) - 1
        #注意index < right不正确
        while index <= right:
            if A[index] == 0:
                A[left], A[index] = A[index], A[left]
                left += 1
                index += 1
            elif A[index] == 1:
                index += 1
            else:
                A[right], A[index] = A[index], A[right]
                right -= 1
#主函数
if __name__ == '__main__':
    A = [1, 0, 1, 2]
    print("初始数组：", A)
    solution = Solution()
    solution.sortColors(A)
    print("结果：", A)