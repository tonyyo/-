class Solution:
    def maxDiffSubArrays(self, nums):
        size = len(nums)
        maxDiff = 0
        for i in range(1, size):
            temp1 = nums[0: i]
            temp2 = nums[i : size]  # 这种边界的处理问题尤其要注意
            temp1_min = self.minsubArrays(temp1)
            temp1_max = self.maxSubArrays(temp1)
            temp2_min = self.minsubArrays(temp2)
            temp2_max = self.maxSubArrays(temp2)

            maxDiff = max(abs(temp2_max - temp1_min), abs(temp1_max - temp2_min))
        return maxDiff

    def maxSubArrays(self, list):
        size = len(list)
        a = list[:]
        aa = list[:]
        for i in range(1, size):
            a[i] = max(a[i], a[i - 1] + a[i])
            aa[i] = max(aa[i - 1], a[i])
        return  aa[size - 1]

    def minsubArrays(self, list):
        size = len(list)
        a = list[:]
        aa = list[:]
        for i in range(1, size):
            a[i] = min(a[i], a[i - 1] + a[i])
            aa[i] = min(aa[i - 1], a[i])
        return  aa[size - 1]

if __name__ == '__main__':
    temp = Solution()
    nums1 = [5,3,1,-4]
    nums2 = [3,-1,6,2]
    print ("输入数组："+str(nums1))
    print ("输出："+str(temp.maxDiffSubArrays(nums1)))
    print ("输入数组："+str(nums2))
    print ("输出："+str(temp.maxDiffSubArrays(nums2)))