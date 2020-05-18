class Solution:
    def longestIncreasingContinuousSubsequence(self, A):
        if not A:
            return 0
        longest, incr, desc = 1, 1, 1
        for i in range(1, len(A)):
            if A[i] > A[i - 1]:
                incr += 1
                desc = 1
            elif A[i] < A[i - 1]:
                incr = 1
                desc += 1
            else:
                incr = 1
                desc = 1
            longest = max(longest, max(incr, desc))
        return longest

    def longestIncreasingContinuousSubsequence(self, A):
        size = len(A)
        inc, desc = 1, 1
        longest = 1
        for i in range(1, size):
            if A[i] > A[i - 1]:
                inc += 1
                desc = 1
            elif A[i] < A[i - 1]:
                desc += 1
                inc = 1
            else:
                inc = 1
                desc =1
            longest = max(longest, inc, desc)
        return longest

if __name__ == '__main__':
    temp = Solution()
    nums1 = [6, 5, 4, 3, 2]
    nums2 = [2, 1, 2, 3, 4, 1, 2, 1, 2, 3, 2, 1]
    print("输入：" + str(nums1))
    print("输出：" + str(temp.longestIncreasingContinuousSubsequence(nums1)))
    print("输入：" + str(nums2))
    print("输出：" + str(temp.longestIncreasingContinuousSubsequence(nums2)))
