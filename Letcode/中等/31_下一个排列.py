class Solution:
    def nextPermutation(self, nums: [int]) -> None:
        N, flag = len(nums), False
        for i in range(N - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                nums[i:] = sorted(nums[i:])
                for j in range(i, N):
                    if nums[i - 1] < nums[j]:
                        nums[i - 1], nums[j] = nums[j], nums[i - 1]
                        flag = True
                        break
            if flag:
                break
        if not flag:
            nums.sort()
if __name__ == '__main__':
    solution = Solution()
    nums = [3,2,1]
    solution.nextPermutation(nums)
    print(nums)


