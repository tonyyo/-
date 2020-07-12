class Solution():
    def beibao(self, weight, values, amount):
        N = len(weight)
        dp = [0] * (amount + 1) # 背包容量为i时的最大满意度为dp[i]
        for i in range(N):
            for j in range(amount, weight[i] - 1, -1):
                    dp[j] = max(dp[j], dp[j - weight[i]] + values[i])
        print(dp)
        return dp[-1]

if __name__ == '__main__':
    N, amount = list(map(int, input().split()))
    weight, values, count = [], [], []
    for i in range(N):
        w, v, c = list(map(int, input().split()))
        for _ in range(c):
            weight.append(w)
            values.append(v)
    solution = Solution()
    print(solution.beibao(weight, values, amount))