class Solution:
    def permute(self, nums: [int], m) -> [[int]]:
        res = []
        self.backTrack(nums, 0, res, [], m)
        return res

    def backTrack(self, nums, k, res, temp, m):  # 从k开始从候选集合中选择元素
        if len(temp) == m:  # 当选择的元素数量达到给定数组的长度时，表明没有了候选元素，为一种排列
            res.append(temp[:])
            return
        for i in range(k, len(nums)):  # k之后的元素都是候选元素
            temp.append(nums[i])        # 组合不需交换，因为不能重复
            self.backTrack(nums, i + 1, res, temp, m)
            temp.pop()

if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2, 3, 4]
    print(solution.permute(nums, 3))
