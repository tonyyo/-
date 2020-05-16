class Solution:
    def searchInsert1(self, A, target):
        if len(A) == 0:
            return 0
        start, end = 0, len(A) - 1
        # first position >= target
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] >= target:
                end = mid
            else:
                start = mid
        if A[start] >= target:
            return start
        if A[end] >= target:
            return end
        return len(A)

    def searchInsert(self, A, target):
        size = len(A)
        left, right = 0, size - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if target <= A[mid]:
                right = mid
            else:
                left = mid
        return right

if __name__ == '__main__':
    temp = Solution()
    List1 = [1, 2, 4, 5]
    target = 4
    print(("输入：" + str(List1) + "  " + str(target)))
    print(("输出：" + str(temp.searchInsert(List1, target))))
