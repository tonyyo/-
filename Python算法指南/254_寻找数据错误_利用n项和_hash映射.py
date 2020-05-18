class Solution:
    def findErrorNums1(self, nums):
        n = len(nums)
        hash = {}
        result = []
        sum = 0
        for num in nums:
            if num in hash:
                result.append(num)
            else:
                hash[num] = 1
                sum += num
        result.append(int(n * (n + 1) / 2) - sum)
        return result

    def findErrorNums(self, nums):
        size = len(nums)
        hash = {}
        result = []
        sum = 0
        for i in range(size):
            if nums[i] in hash:
                result.append(nums[i])
            else:
                hash[nums[i]] = 1
                sum += nums[i]
        result.append(int(size * (size + 1)/ 2) - sum)
        return result

#主函数
if __name__ == "__main__":
    nums = [1, 2, 2, 4]
    #创建对象
    solution = Solution()
    print("输入的初始数组是：", nums)
    print("输出的结果是：", solution.findErrorNums(nums))