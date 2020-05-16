class Solution:
    def searchRange2(self, A, target):
        if len(A) == 0:
            return [-1, -1]
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] < target:
                start = mid
            else:
                end = mid
        if A[start] == target:
            leftBound = start
        elif A[end] == target:
            leftBound = end
        else:
            return [-1, -1]
        start, end = leftBound, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] <= target:
                start = mid
            else:
                end = mid
        if A[end] == target:
            rightBound = end
        else:
            rightBound = start
        return [leftBound, rightBound]

    def searchRange(self, A, target):
        size = len(A)
        start, end = 0, 0
        for i in range(size):
            if A[i] == target:
                start = i
        for i in range(size - 1, -1, -1):
            if A[i] == target:
                end = i
        if start and end:
            return [start, end]
        else:
            return [-1, -1]

if __name__ == '__main__':
    temp = Solution()
    List1 = [1, 2, 4, 5, 6, 7, 8]
    target = 8
    print(("输入：" + str(List1) + "  " + str(target)))
    print(("输出：" + str(temp.searchRange(List1, target))))
