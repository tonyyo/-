class Solution:
    def minSubArray(self, nums):
        MIN = 65536
        SUM = nums[0]
        for i in range(1, len(nums)):
            SUM = SUM + nums[i] if SUM < 0 else nums[i] # SUM > 0有害于最小和
            MIN = min(MIN, SUM)
        return MIN

if __name__ == '__main__':
    temp = Solution()
    List1 = [1, -1, -2, 1]
    List2 = [3, -2, 2, 1]
    print("输入：" + str(List1))
    print(("输出：" + str(temp.minSubArray(List1))))
    print("输入：" + str(List2))
    print(("输出：" + str(temp.minSubArray(List2))))
