class Solution:
    def continuousSubarraySum(self, A):
        max_sum = -65536
        ans = {}
        size = len(A)
        start, end = 0, 0
        for i in range(size):
            end = i
            prefix_sum = max_sum + A[i]
            if A[i] > prefix_sum:
                start = i        # 关键, 当前n-1项和的最大值对第n项无法起积极作用时, 果断抛弃前n-1项
                prefix_sum = A[i]
            max_sum = max(max_sum, prefix_sum)
            ans.update({max_sum : [start, end]})  # value可以放各种各样的类型, 用update添加指定字典, 所以要用大括号
        print(ans)
        return ans[max(ans)]  # max计算的是key的最大值

# 主函数
if __name__ == "__main__":
    nums = [-3, 1, 3, -3, 4]
    # 创建对象
    solution = Solution()
    print("输入的数组是 ：", nums)
    print("使得和最大的子数组是:", solution.continuousSubarraySum(nums))
