class Solution:
    def firstWillWin(self, values):
        if not values:
            return False
        if len(values) <= 2:
            return True
        n = len(values)
        #动态规划
        f = [0] * 3
        prefix_sum = [0] * 3
        f[(n - 1) % 3] = prefix_sum[(n - 1) % 3] = values[n - 1]
        #按从n-1～0的相反顺序遍历值
        for i in range(n - 2, -1, -1):
            prefix_sum[i % 3] = prefix_sum[(i + 1) % 3] + values[i]
            f[i % 3] = max(
                values[i] + prefix_sum[(i + 1) % 3] - f[(i + 1) % 3],
                values[i] + values[i + 1] + prefix_sum[(i + 2) % 3] - f[(i + 2) % 3],
            )
        return f[0] > prefix_sum[0] - f[0]
#主函数
if __name__=="__main__":
    values=[1,2,4]
    #创建对象
    solution=Solution()
    print("输入的数组是：",values)
    print("第一个玩家赢的情况是:",solution.firstWillWin(values))