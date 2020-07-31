class Solution:
    def firstMissingPositive(self, nums: [int]) -> int:
        N = len(nums)
        for i in range(N):
            if nums[i] <= 0:
                nums[i] = N + 1  # 因为要利用-1进行打标记

        for i in range(N):
            index = abs(nums[i])
            if index <= N:
                # 实际位置要偏小一位, 而且单纯取负，还能保留原有值, 而且要防止负负得正的情况
                nums[index - 1] = -abs(nums[index - 1])

        for i in range(N):
            if 0 < nums[i]:
                return i + 1

        return N + 1

if __name__ == '__main__':
    solution = Solution()
    print(solution.firstMissingPositive([2,1]))