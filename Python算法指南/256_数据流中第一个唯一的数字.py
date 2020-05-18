class Solution:
    def firstUniqueNumber2(self, nums, number):
        if not nums:
            return -1
        num_cnt = {}
        ans = None
        for n in nums:
            num_cnt[n] = num_cnt.get(n, 0) + 1
            if n == number:
                break
        for k, v in num_cnt.items():
            if v == 1:
                ans = k
                break
        if ans is None or number not in num_cnt:
            return -1
        return k

    def firstUniqueNumber(self, nums, number):
        size = len(nums)
        i = 0
        hash = {}
        while nums[i] != number:
            if nums[i] not in hash.keys():
                hash[nums[i]] = 1
            else:
                hash[nums[i]] += 1
            i += 1
        print(hash)
        for key in hash.keys():
            if hash[key] == 1:
                return key
        return None
#主函数
if __name__ == "__main__":
    nums = [1, 2, 2, 1, 3, 4, 4, 5, 6]
    number = 5
    #创建对象
    solution = Solution()
    print("初始化的数组是：", nums, "给定的终止数字是：", number)
    print("终止数字到达时的第一个唯一数字是：", solution.firstUniqueNumber(nums, number))