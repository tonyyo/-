class Solution:
    def combine(self, n: int, k: int) -> [[int]]:
        nums = []
        for i in range(1, n + 1):
            nums.append(i)
        res = []
        self.backtrack(nums, res, k, 0, [])
        return res

    def backtrack(self, nums, res, k, pos, temp):
        if len(temp) == k:
            res.append(temp[:])
        for i in range(pos, len(nums)):
            temp.append(nums[i])
            self.backtrack(nums, res, k, i + 1, temp)
            temp.pop()
if __name__ == '__main__':
    solution = Solution()
    print(solution.combine(4, 2))
