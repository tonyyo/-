class Solution(object):
    def merge(self, nums1, m, nums2, n):
        M, N = m - 1, n - 1  # 初始化双指针
        while M >= 0 and N >= 0:
            if nums1[M] <= nums2[N]:
                nums1[M + N + 1] = nums2[N]  # 用双指针表示新数组的索引时要注意
                N -= 1
            else:
                nums1[M + N + 1] = nums1[M]
                M -= 1
        while M < 0 and N >= 0:  # M大于0的话，本身就在原位置， 不用动
            nums1[N] = nums2[N]
            N -= 1
        return nums1

if __name__ == '__main__':
    solution = Solution()
    num1 = []
    print(solution.merge(nums1=[1,2,3,0,0,0], m = 3, nums2=[2,5,6], n = 3))

