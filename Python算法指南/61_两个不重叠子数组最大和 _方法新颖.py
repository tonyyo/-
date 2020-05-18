class Solution:
    def maxTwoSubArrays(self, nums):
        length = len(nums)
        mx = 0
        for i in range(1, length):
            temp1 = nums[0:i]  # 如果这样取子数组时两端的值相等, 那么取得的值将是空数组
            temp2 = nums[i:length]
            max_sum = self.maxSubArrays(temp1) + self.maxSubArrays(temp2)
            mx = max(mx, max_sum)
        return mx

    def maxSubArrays(self, arr):
        length = len(arr)
        prefix_sum = 0
        max_sum = 0
        ans = []
        for i in range(length):
            prefix_sum = max_sum + arr[i]
            max_sum = max(prefix_sum, arr[i])
            ans.append(max_sum)
        return max(ans)

if __name__ == '__main__':
    temp = Solution()
    nums1 = [1, 3, -1, 2, -1, 2]
    print(("输入：" + str(nums1)))
    print(("输出：" + str(temp.maxTwoSubArrays(nums1))))

# class Solution:
#     def maxTwoSubArrays(self, nums):
#         n = len(nums)
#         a = nums[:]
#         aa = nums[:]
#         for i in range(1, n):
#             a[i] = max(nums[i], a[i-1] + nums[i])  # 先计算两两之间的值的最大值
#             aa[i] = max(a[i], aa[i-1])  # max比较列表大小与比较字符串一样, 先看首元素, 感觉不需要这么麻烦
#         b = nums[:]
#         bb = nums[:]
#         for i in range(n-2, -1, -1):
#             b[i] = max(nums[i], b[i+1] + nums[i])
#             bb[i] = max(b[i], bb[i+1])
#         mx = -65535
#         print(aa)
#         print(bb)
#         for i in range(n - 1):
#             mx = max(aa[i]+b[i+1], mx) #把数组分为两部分, 分别求出每一部分的最大和
#         return mx
