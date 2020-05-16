class Solution:
    def find_upper_closest(self, A, target):  #找到大于或等于target的第一个数, 然后就可以找到左边与Target相邻的那个数
        left, right = 0, len(A) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if A[mid] < target:
                left = mid
            else:
                right = mid
            return right  # 只有可能返回right

    def is_left_closer(self, A, target, left, right):  #如果左边的数更近, 放回true
        if left < 0:
            return False
        if right >= len(A) - 1:
            return False
        return target - A[left] <= A[right] - target

    def kClosestNumbers(self, A, target, k):
        ans = []
        right = self.find_upper_closest(A, target)
        left = right - 1
        for _ in range(k):
            if self.is_left_closer(A, target, left, right):
                ans.append(A[left])
                left -= 1
            else:
                ans.append(A[right])
                right += 1
        return ans

if __name__ == '__main__':
    solution = Solution()
    A = [1, 4, 6, 8]
    print(solution.kClosestNumbers(A, 3, 3))

# class Solution:
#     def find_upper_closest(self, A, target):  #找到大于或等于target的第一个数, 然后就可以找到左边与Target相邻的那个数
#         start, end = 0, len(A) - 1
#         while start + 1 < end:  # 二分法的简单引用, 不需要加加,减减操作
#             mid = (start + end) // 2
#             if A[mid] >= target:
#                 end = mid
#             else:
#                 start = mid
#         if A[start] >= target:
#             return start  # 如果该条语句满足, 那么下面那条return语句将不会执行
#         if A[end] >= target:
#             return end
#         return end + 1
#
#     def is_left_closer(self, A, target, left, right):  #如果左边的数更近, 放回true
#         if left < 0:
#             return False
#         if right >= len(A):
#             return True
#         return target - A[left] <= A[right] - target #因为数组A是按升序排列的, 所以可以直接这么判断
#
#     def kClosestNumbers(self, A, target, k):
#         right = self.find_upper_closest(A, target)
#         left = right - 1
#         result = []
#         for _ in range(k):  #找到了target两旁的数后, 进行k次循环, 找到k个数
#             if self.is_left_closer(A, target, left, right):  #比较谁更近
#                 result.append(A[left])
#                 left -= 1
#             else:
#                 result.append(A[right])
#                 right += 1
#         return result
