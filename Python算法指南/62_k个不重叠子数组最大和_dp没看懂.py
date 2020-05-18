class Solution:
    def maxSubArray(self, nums, k):
        MIN = - 2 ** 32
        n = len(nums)
        array = [0]
        for num in nums:
            array.append(num)
        # include the last num
        ans1 = [[MIN for i in range(k + 1)] for j in range(n + 1)] # 列为k+1, 行为n+1
        # do not include the last num
        ans2 = [[MIN for i in range(k + 1)] for j in range(n + 1)]
        for i in range(n + 1):
            ans1[i][0] = 0
            ans2[i][0] = 0
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                ans1[i][j] = max(ans1[i - 1][j] + array[i], ans1[i - 1][j - 1] + array[i], ans2[i - 1][j - 1] + array[i])
                ans2[i][j] = max(ans1[i - 1][j], ans2[i - 1][j])
        return max(ans1[n][k], ans2[n][k])
# 主函数
if __name__ == '__main__':
    nums = [-1, 4, -2, 3, -2, 3]
    k = 2
    print("初始数组和k值：", nums, k)
    solution = Solution()
    print("不重叠子数组的和：", solution.maxSubArray(nums, k))