class Solutioin:
    def quickSort(self, A, start, end):  # 快速排序需要一个开始位置和一个结束位置
        if start >= end:
            return
        pivot = A[start]
        left = start
        right = end
        while left < right:
            while A[right] > pivot and left < right: # right遇到相等的还是要交换到左边，所以不能跳过
                right -= 1
            while A[left] <= pivot and left < right: # left遇到相等的可以跳过，因为从自身开始
                left += 1
            if left < right:
                A[left], A[right] = A[right], A[left]
        A[start], A[left] = A[left], A[start]
        self.quickSort(A, start, left - 1) # left == right跳出循环，中间元素不需要再比较
        self.quickSort(A, right + 1, end) # 如果这里不进行加1减1操作，将超出递归次数

    def sortInteger(self, A):
        self.quickSort(A, 0, len(A) - 1)
if __name__ == '__main__':
    A = [3, 2, 1, 4, 5, 9, 20, 7]
    solution = Solutioin()
    solution.sortInteger(A)
    print(A)


