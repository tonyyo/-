class Solution:
    def longestIncreasingContinuousSubsequence(self, A):
        inc, dec = 1, 1 # 因为至少会存在一个递增和递减
        maxLength = 0
        for i in range(1, len(A)): # 从1开始，就是默认第一个元素是递增或者递减
            if A[i] > A[i - 1]:
                inc += 1
                dec = 1
            elif A[i] < A[i - 1]:
                dec += 1
                inc = 1
            else:  # 相等的时候其实LICS已经结束，该对两个指针重新初始化为1
                inc = 1
                dec = 1
            maxLength = max(maxLength, max(inc, dec)) # 每次循环都记录一次最大值，十分明智的选择
        return  maxLength


if __name__ == '__main__':
    temp = Solution()
    nums1 = [6, 5, 4, 3, 2]
    nums2 = [2, 1, 2, 3, 4, 1, 2, 1, 2, 3, 2, 1]
    print("输入：" + str(nums1))
    print("输出：" + str(temp.longestIncreasingContinuousSubsequence(nums1)))
    print("输入：" + str(nums2))
    print("输出：" + str(temp.longestIncreasingContinuousSubsequence(nums2)))
