class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        map = dict()
        if len(nums) < 2:
            return []
        for k, v in enumerate(nums):
            if target - v in map:
                return [map[target - v], k]
            else:
                map[v] = k
        return []