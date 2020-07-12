from itertools import permutations


class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        strN = str(N)
        strList = list(permutations(strN, len(strN))) # 直接给字符串全排列输出字符串数组
        for s in strList:
            if s[0] == '0':
                continue
            s = "".join(s)
            i = int(s)
            if i & (i - 1) == 0:
                return True
        return False



    # def reorderedPowerOf2(self, N: int) -> bool:
    #     nums = []
    #     while N != 0:
    #         yu = N % 10
    #         nums.append(yu)
    #         N = N // 10
    #     result = []
    #     self.permutations(nums, result, 0)
    #     finalRes = []
    #     for x in result:
    #         x = int(x)
    #         if x & (x - 1) == 0:
    #             finalRes.append(x)
    #     return True if len(finalRes) != 0 else False
    #
    # def permutations(self, nums, result, k):
    #     N = len(nums)
    #     if k == N:
    #         if nums[0] != 0:
    #             stringNum = "".join([str(x) for x in nums])
    #             result.append(stringNum)
    #         return
    #     for i in range(k, len(nums)): # k个候选集
    #         nums[k], nums[i] = nums[i], nums[k]
    #         self.permutations(nums, result, k + 1) # 选择k次
    #         nums[k], nums[i] = nums[i], nums[k]

if __name__ == '__main__':
    solution = Solution()
    N = 1402
    print(solution.reorderedPowerOf2(N))