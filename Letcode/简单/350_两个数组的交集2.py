from collections import defaultdict


class Solution:
    def intersect(self, nums1: [int], nums2: [int]) -> [int]:
        M, N = len(nums1), len(nums2)
        res = []
        hash = defaultdict(int)
        for i in range(M):
            hash[nums1[i]] += 1 # 统计元素和次数
        for num in nums2:
            if num in hash and hash[num] != 0:
                res.append(num)
                hash[num] -= 1
        return res