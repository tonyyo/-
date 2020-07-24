import time


class Solution:
    def findMin(self, nums):
        if not nums:
            return -1
        start, end = 0, len(nums) - 1
        target = nums[-1]  # 将target赋值为最后一个元素, 相当于取了排序数组的中间元素, 其实可以直接
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] <= target:  # 往中间找才能找到最小值
                end = mid
            else:
                start = mid
        print(nums[start])
        print(nums[end])
        return min(nums[start], nums[end])

if __name__ == '__main__':
    temp = Solution()
    List1 = [6, 7, 1, 2, 3, 4, 5]
    print(("输入：" + str(List1)))
    start = time.clock()
    print(("输出：" + str(temp.findMin(List1))))
    print(time.clock() - start)
