class Solution:
    def partitionArray(self, nums, k):
        start, end = 0, len(nums) - 1
        while start <= end:
            while start <= end and nums[start] < k:
                start += 1
            while start <= end and nums[end] >= k:
                end -= 1
            if start <= end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        return nums

    def partitionArray2(self, nums, k):
        size = len(nums)
        left, right = 0, size - 1
        for i in range(size):
            while left <= right:
                while nums[left] < k:
                    left += 1
                while nums[right] >= k:
                    right -= 1
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        return nums



if __name__ == '__main__':
    temp = Solution()
    List1 = [5, 1, 4, 2, 3]
    num = 2
    print(("输入：" + str(List1) + "  " + str(num)))
    print(("输出：" + str(temp.partitionArray(List1, num))))
