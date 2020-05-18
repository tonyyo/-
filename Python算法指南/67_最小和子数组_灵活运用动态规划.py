class Solution:
    def minSubArray(self, nums):
        size = len(nums)
        prefix_sum = 0
        min_sum = 65536
        ans = []
        for i in range(size):
            prefix_sum = min(prefix_sum + nums[i], nums[i])
            ans.append(prefix_sum)
        return min(ans)

if __name__ == '__main__':
    temp = Solution()
    List1 = [1, -1, -2, 1]
    List2 = [3, -2, 2, 1]
    print("输入：" + str(List1))
    print(("输出：" + str(temp.minSubArray(List1))))
    print("输入：" + str(List2))
    print(("输出：" + str(temp.minSubArray(List2))))
