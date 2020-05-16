class Solution:
    def maxAverage(self, nums, k):  # https://www.jianshu.com/p/97c976bd2f27
        if not nums:
            return 0
        start, end = min(nums), max(nums)
        while end - start > 1e-5:
            mid = (start + end) / 2
            if self.check_subarray(nums, k, mid): # 如果
                start = mid
            else:
                end = mid
        return start

    def check_subarray(self, nums, k, average):
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num - average)

        min_prefix_sum = 0
        for i in range(k, len(nums) + 1):
            if prefix_sum[i] - min_prefix_sum >= 0:
                return True
            min_prefix_sum = min(min_prefix_sum, prefix_sum[i - k + 1])
        return False


if __name__ == '__main__':
    temp = Solution()
    nums = [5, 3, -4, 6, -7, 2, -1]
    k = 5
    print(("输入：" + str(nums) + "  " + str(k)))
    print(("输出：" + str(temp.maxAverage(nums, k))))