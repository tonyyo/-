class Solution:
    def search(self, A, target):
        if not A:
            return -1
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] >= A[start]:
                if A[start] <= target <= A[mid]:
                    end = mid
                else:
                    start = mid
            else:
                if A[mid] <= target <= A[end]:
                    start = mid
                else:
                    end = mid
        if A[start] == target:
            return start
        if A[end] == target:
            return end
        return -1

    def search2(self, A, target):
        left, right = 0, len(A) - 1
        while left < right:
            mid = (left + right) // 2
            if A[mid] > A[right]:
                left = mid + 1
            else:
                right = mid
        middle = left
        if target > A[-1]:
            start, end = 0, middle - 1
            while start + 1 < end:  # 只用mid代替移动的话, 必须这样, 否则无法跳出循环
                mid = (start + end) // 2
                if A[mid] < target:
                    start = mid
                else:
                    end = mid
            return end
        else:
            start, end = middle, len(A) - 1
            while start + 1 < end:
                mid = (start + end) // 2
                if A[mid] < target:
                    start = mid
                else:
                    end = mid
            return end


if __name__ == '__main__':
    temp = Solution()
    List1 = [6, 7, 8, 9, 1, 2, 3, 4, 5];
    k1 = 8
    print(("输出：" + str(temp.search2(List1, k1))))
