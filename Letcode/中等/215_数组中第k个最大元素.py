class Solution:
    def findKthLargest(self, nums: [int], k: int) -> int:
        N = len(nums)
        for i in range(N - 1, N - k - 1, -1):
            self.heapSort(nums, i)
            nums[0], nums[i] = nums[i], nums[0]
        print(nums)
        return nums[-k]

    def heapSort(self, nums, tail):
        parent = tail // 2 - 1 if tail & 1 == 0 else tail // 2  # 因根节点是0，所以求父节点需分奇偶
        while parent >= 0:
            if 2 * parent + 2 <= tail:
                index = 2 * parent + 1 if nums[2 * parent + 1] >= nums[2 * parent + 2] else 2 * parent + 2
                if nums[index] > nums[parent]:
                    nums[index], nums[parent] = nums[parent], nums[index]
            else:
                if nums[2 * parent + 1] > nums[parent]:
                    nums[2 * parent + 1], nums[parent] = nums[parent], nums[2 * parent + 1]
            parent -= 1

if __name__ == '__main__':
    solution = Solution()
    nums = [3,1,2,4]
    print(solution.findKthLargest(nums, 2))
