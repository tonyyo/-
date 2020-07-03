class Solution:
    def jumpFloorII(self, number):
        if number == 1:
            return 1
        if number == 2:
            return 2
        else:
            dp = [1, 1, 2]  # dp[n]表示跳上第n阶台阶的方法数
            for i in range(3, number + 1):
                dp.append(sum(dp))  # 可能从前面的任何一个台阶上一步跳上来，所以将所以的情况加起来即可
            return dp[-1]

if __name__ == '__main__':
    solution = Solution()
    print(solution.jumpFloorII(3))