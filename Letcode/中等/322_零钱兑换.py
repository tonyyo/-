import sys


class Solution:
    def coinChange(self, coins: [int], amount: int) -> int:
        dp = [sys.maxsize] * (amount + 1)  # 凑成总金额为n所需最小硬币数
        dp[0], N = 0, len(coins)  # 总金额为0时是凑不出来的
        for i in range(N):
            for j in range(coins[i], amount + 1):
                dp[j] = min(dp[j], dp[j - coins[i]] + 1)
        print(dp)
        return dp[amount] if dp[amount] != sys.maxsize else -1

if __name__ == '__main__':
    solution = Solution()
    coins = [1,2,5]
    amount = 11
    print(solution.coinChange(coins, amount))


