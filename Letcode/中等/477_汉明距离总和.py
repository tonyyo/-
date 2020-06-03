class Solution:
    def totalHammingDistance(self, nums: [int]) -> int:
        countSum = 0
        N = len(nums)
        for i in range(64):
            count = 0
            for num in nums:
                if num & (1 << i) != 0:
                    count += 1
            countSum += count * (N - count)
        return countSum
if __name__ == '__main__':
    solution = Solution()
    arr = [4, 12, 2]
    print(solution.totalHammingDistance(arr))
