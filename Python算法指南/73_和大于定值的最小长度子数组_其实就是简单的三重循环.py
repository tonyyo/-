class Solution:
    def minimumSize(self, nums, s):
        if nums is None or len(nums) == 0:
            return -1
        n = len(nums)
        minLength = n + 1
        sum = 0
        j = 0
        for i in range(n):
            while j < n and sum < s:
                sum += nums[j]
                j += 1
            if sum >= s:
                minLength = min(minLength, j - i)
            sum -= nums[i]
        if minLength == n + 1:
            return -1
        return minLength

if __name__ == '__main__':
    temp = Solution()
    List1 = [1, 2, 3, 4, 5]
    nums1 = 10
    print(("输入：" + str(List1) + "  " + str(nums1)))
    print(("输出：" + str(temp.minimumSize2(List1, nums1))))
