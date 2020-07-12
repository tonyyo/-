class Solution:
    def search(self, nums: [int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:  # 必须等于，因为要计算left == right == mid的情况
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:   # 要加上等于， 因为//整除符号向左偏移
                if nums[left] <= target < nums[mid]: # 必须要加上左边界，因为可能还会在右边
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
if __name__ == '__main__':
    solution = Solution()
    nums = [3,1]
    print(solution.search(nums,1))