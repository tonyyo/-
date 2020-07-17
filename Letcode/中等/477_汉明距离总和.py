class Solution:
    def totalHammingDistance(self, nums: [int]) -> int:
        countSum = 0
        for i in range(64):
            count = 0   # 各数字在对应位上1的个数和
            for num in nums:
                if num & (1 << i) != 0:
                    count += 1
            countSum += count * (len(nums) - count)
        return countSum

if __name__ == '__main__':
    solution = Solution()
    arr = [4, 12, 2]
    print(solution.totalHammingDistance(arr))
