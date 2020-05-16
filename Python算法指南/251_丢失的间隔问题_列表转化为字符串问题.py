class Solution:
    def findMissingRanges2(self, nums, lower, upper):
        result = []
        nums = [lower-1] + nums + [upper+1]
        for i in range(1, len(nums)):
            l = nums[i-1]
            h = nums[i]
            if h - l >= 2:
                if h - l == 2:
                    result.append(str(l+1))
                else:
                    result.append(str(l+1)+"->"+str(h-1))
        return result

    def findMissingRanges(self, nums, lower, upper):
        size = len(nums)
        paixu = [i for i in range(lower, upper + 1)]
        res = []
        ans = []
        if nums[0] > lower:
            res.append(paixu[lower : nums[0]])
        for i in range(1, size):
            if nums[i] > nums[i - 1]:
                res.append(paixu[nums[i - 1] + 1: nums[i]])
        if nums[-1] < upper:
            res.append(paixu[nums[-1] + 1 : upper + 1])
        for x in res:
            if len(x) == 1:
                ans.append(''.join(str(i) for i in x))
            elif len(x) > 1:
                string = ''.join(str(x[0]) + " -> " + str(x[-1]))
                ans.append(string)
        return ans


#主函数
if __name__ == "__main__":
    nums = [0, 1, 3, 50, 75]
    lower=0
    upper=99
    #创建对象
    solution = Solution()
    print("输入的整数数组nums= ：", nums, "lower=",lower, "upper=",upper)
    print("缺少的范围结果是:", solution.findMissingRanges(nums,lower,upper))