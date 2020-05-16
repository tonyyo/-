class Solution:
    def maxChaTwoArray(self, arr):
        MAX = 0
        for i in range(1, len(arr)):
            temp1 = arr[0 : i]
            temp2 = arr[i : ]
            MAX = max(self.maxSumArray(temp1) - self.minSumArray(temp2),
                      self.maxSumArray(temp2) - self.minSumArray(temp1), MAX)
        return MAX

    def maxSumArray(self, arr):
        SUM, MAX = arr[0], arr[0]
        for i in range(1, len(arr)):
            SUM = SUM + arr[i] if SUM >= 0 else arr[i]
            MAX = max(MAX, SUM)
        return MAX

    def minSumArray(self, arr):
        SUM, MIN = arr[0], arr[0]
        for i in range(1, len(arr)):
            SUM = SUM + arr[i] if SUM <= 0 else arr[i]
            MIN = max(MIN, SUM)
        return MIN

if __name__ == '__main__':
    temp = Solution()
    nums1 = [5,3,1,-4]
    nums2 = [3,-1,6,2]
    print ("输入数组："+str(nums1))
    print ("输出："+str(temp.maxChaTwoArray(nums1)))
    print ("输入数组："+str(nums2))
    print ("输出："+str(temp.maxChaTwoArray(nums2)))