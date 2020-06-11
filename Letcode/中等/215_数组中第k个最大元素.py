import heapq


class Solution:
    def findKthLargest(self, nums: [int], k: int) -> int:
        res = heapq.nlargest(k, nums)
        return res[-1]
if __name__ == '__main__':
    solution = Solution()
    nums = [3,2,3,1,2,4,5,5,6]
    print(solution.findKthLargest(nums, 4))
