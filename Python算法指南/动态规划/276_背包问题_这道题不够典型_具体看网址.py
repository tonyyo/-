class Solution:
    def backPack(self, amount, coins):
        temp, ans = [], []
        self.dfs(amount, coins, temp, ans)
        return ans

    def dfs(self, amount, coins, temp, ans):
        if sum(temp) == amount:
            temp.sort()
            if temp not in ans:  # 因为重复使用，所以要求去重
                ans.append(temp[:])
            return
        if sum(temp) > amount:
            return
        for i in range(len(coins)):
            temp.append(coins[i])
            self.dfs(amount, coins, temp, ans) # 此处不能截断coins，因为要重复使用coins数组里的值
            temp.pop()



#主函数
if __name__ == '__main__':
    amount = 5
    coins =  [1, 2, 5]
    coins = sorted(coins, reverse=True)
    solution = Solution()
    print(solution.backPack(amount, coins))