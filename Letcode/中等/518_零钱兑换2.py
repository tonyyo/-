class Solution:
    def change1(self, amount: int, coins: [int]) -> int:
        dp = [0] * (amount + 1) # 凑成总金额为n的组合数
        N = len(coins)
        dp[0] = 1
        for i in range(N):
            for j in range(coins[i], amount + 1):
                    dp[j] += dp[j - coins[i]]
            print(dp)
        return dp[amount]

if __name__ == '__main__':
    solution = Solution()
    print(solution.change(5, [1, 2, 5]))