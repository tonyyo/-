class Solution(object):
    def singleNonDuplicate(self, nums): # 在一个奇数位的排序数组中找到落单的那个数
        N = len(nums)
        low, high = 0, N - 1
        while low < high:
            mid = (low + high) // 2
            if mid % 2 == 1:
                mid -= 1   # 让mid落入偶数位，这样左右都会是偶数位个数
            if nums[mid] == nums[mid + 1]: # 落单的数在右边
                low = mid + 2
            else:
                high = mid
        return nums[low]

    def singleNonDuplicate1(self, nums):  # 利用位异或的方式
        N = len(nums)
        result = nums[0]
        for i in range(1, N):
            result ^= nums[i]
        return result

if __name__ == '__main__':
    solution = Solution()
    print(solution.singleNonDuplicate1(nums=[1,1,2,2,3,4,4]))