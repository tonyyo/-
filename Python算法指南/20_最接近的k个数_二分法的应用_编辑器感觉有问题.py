class Solution:
    def find_upper_closest(self, A, target):
        left, right = 0, len(A) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if target > A[mid]:
                left = mid
            elif target <= A[mid]:
                right = mid
        return right

    def kClosestNumbers(self, A, target, k):
        ans = []
        right = self.find_upper_closest(A, target)
        left = right - 1
        while k != 0:
            if (A[right] - target) > (target - A[left]) or right >= len(A):
                ans.append(A[left])
                right += 1
                k -= 1
            elif A[right] - target < target - A[left] or left < 0:
                ans.append(A[right])
                left -= 1
                k -= 1
            elif A[right] - target == target - A[left]:
                ans.append(A[left])
                ans.append(A[right])
                left -= 1
                right += 1
                k -= 2
        return ans


if __name__ == '__main__':
    solution = Solution()
    A = [1, 2, 3]
    print(solution.kClosestNumbers(A, 2, 3))
