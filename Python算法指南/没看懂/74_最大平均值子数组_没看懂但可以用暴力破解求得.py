class Solution:
    def maxAverage(self, nums, k):  # https://www.jianshu.com/p/97c976bd2f27
        SUM, MAX, length = nums[0], nums[0], 1
        for i in range(1, len(nums)):
            if (SUM + nums[i]) / (length + 1) >= nums[i]:
                length += 1
                SUM = SUM + nums[i]
                AVG = (SUM + nums[i]) / length
            else:
                SUM = nums[i]
                AVG = nums[i]
                length = 1
            MAX = max(AVG, MAX)
        return MAX

if __name__ == '__main__':
    temp = Solution()
    nums = [5, 3, -4, 6, -7, 2, -1]
    k = 5
    print(("输入：" + str(nums) + "  " + str(k)))
    print(("输出：" + str(temp.maxAverage(nums, k))))
