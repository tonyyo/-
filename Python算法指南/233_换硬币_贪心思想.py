class Solution:
    def coinChange1(self, coins, amount):
        import math
        dp = [math.inf] * (amount + 1)
        dp[0] = 0
        for i in range(amount + 1):
            for j in range(len(coins)):
                if i >= coins[j] and dp[i - coins[j]] < math.inf:
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1)
        if dp[amount] == math.inf:
            return -1
        else:
            return dp[amount]

    def coinChange(self, coins, amount):
        coins = sorted(coins, reverse=True)
        tmp = []
        self.res = []
        self.dfs(coins, amount, tmp)
        self.res = sorted(self.res, key=lambda x: (x[1]))
        return self.res[0][1]

    def dfs(self, coins, amount, tmp):
        if sum(tmp) == amount:
            tmp = sorted(tmp[:])
            if tmp not in self.res:
                self.res.append([tmp, len(tmp)])
            return
        if sum(tmp) > amount:
            return
        for i in range(len(coins)):
            tmp.append(coins[i])
            self.dfs(coins, amount, tmp)
            tmp.pop()

# 主函数
if __name__ == '__main__':
    coins = [1, 2, 5]
    amount = 11
    print("硬币面额：", coins)
    print("总硬币：", amount)
    solution = Solution()
    print("换取的最小硬币数量：", solution.coinChange(coins, amount))
