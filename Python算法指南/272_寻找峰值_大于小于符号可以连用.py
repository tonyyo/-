class Solution:
    def findPeak(self, A):
        start, end = 1, len(A) - 2
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] < A[mid - 1]:
                end = mid
            elif A[mid] < A[mid + 1]:
                start = mid
            else:
                end = mid
        if A[start] < A[end]:
            return end
        else:
            return start

    def findPeak1(self, A):
        size = len(A)
        result = []
        for i in range(1, size - 1, 1):
            if A[i-1] < A[i] > A[i+1]:
                result.append(A[i])
        return result

if __name__ == '__main__':
    temp = Solution()
    List1 = [2, 5, 3, 4, 6, 7, 5]
    print(("输入：" + str(List1)))
    print(("输出：" + str(temp.findPeak1(List1))))
