class Solution:
    def permute(self, nums: [int]) -> [[int]]:
        res = []
        self.backTrack(nums, 0, res)
        return res

    def backTrack(self, nums, k, res):  # 从k开始从候选集合中选择元素
        if k == len(nums):  # 当选择的元素数量达到给定数组的长度时，表明没有了候选元素，为一种排列
            res.append(nums[:])
            return
        for i in range(k, len(nums)):  # k之后的元素都是候选元素
            nums[i], nums[k] = nums[k], nums[i]
            self.backTrack(nums, k + 1, res)
            nums[i], nums[k] = nums[k], nums[i]

if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2, 3]
    print(solution.permute(nums))
