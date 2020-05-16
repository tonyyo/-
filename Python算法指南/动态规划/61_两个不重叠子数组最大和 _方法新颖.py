class Solution:
    def maxTwoSubArrays(self, nums):
        size = len(nums)
        MAX = 0
        for i in range(1, size):
            temp1 = nums[0 : i]
            temp2 = nums[i : ]
            MAX = max(self.maxSubArrays(temp1) + self.maxSubArrays(temp2), MAX)
        return MAX

    def maxSubArrays(self, arr):
        SUM, MAX = arr[0], arr[0]
        for i in range(1, len(arr)):
            SUM = SUM + arr[i] if SUM > 0 else arr[i]
            MAX = max(MAX, SUM)
        return MAX

if __name__ == '__main__':
    temp = Solution()
    nums1 = [6, 5, 4, 3, 2]
    print(("输入：" + str(nums1)))
    print(("输出：" + str(temp.maxTwoSubArrays(nums1))))
