class Solutioin:
    def quickSort(self, A, start, end):
        if start >= end:
            return
        left, right = start, end
        pivot = A[(start + end) // 2]  # 哨兵应放在外面
        while left < right:   # 等于的话就不用交换了, 所以可以作为出口
            while left < right and A[left] < pivot:
                left += 1
            while left < right and A[right] > pivot:  # 哨兵是可以等于指针的
                right -= 1
            A[left], A[right] = A[right], A[left]
            left += 1
            right -= 1
        self.quickSort(A, start, right)  # 避免用mid了
        self.quickSort(A, left, end)


if __name__ == '__main__':
    A = [3, 2, 1, 4, 5, 9, 20, 7]
    solution = Solutioin()
    solution.quickSort(A, 0, len(A) - 1)
    print(A)
