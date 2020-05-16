class Solution:
    def getSingleNumber(self, nums):
        ans = 0
        for x in nums:
            ans ^= x
        return ans
if __name__ == '__main__':
    solution = Solution()
    nums = [1, 1, 2, 2, 3, 4, 4, 5, 5]
    print(solution.getSingleNumber(nums))
