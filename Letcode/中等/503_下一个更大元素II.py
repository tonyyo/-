class Solution:
    def nextGreaterElements(self, nums: [int]) -> [int]:
        N = len(nums)
        result = [0] * N
        for i in range(N):
            flag = False
            for j in range(1, N):
                if nums[(i + j) % N] > nums[i]:  # 采用取余的方式即可
                    result[i] = nums[(i + j) % N]
                    flag = True
                    break
            if not flag:
                result[i] = -1
        return result