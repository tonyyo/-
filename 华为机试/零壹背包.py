if __name__ == '__main__':
    # 一维解法
    weight = [2, 3, 4, 5]
    value = [3, 4, 5, 6]
    N = len(weight)
    capacity = 8
    dp = [0] * (capacity + 1)  # dp[j]表示为容量为j的背包所能放置的物品最大价值和
    for i in range(N):
        for j in range(capacity, weight[i] - 1, -1):   # 只取容量大于当前物品的背包
            dp[j] = max(dp[j], dp[j - weight[i]] + value[i])
    print(dp[capacity])

    # 二维0/1背包
    # weight = [2, 3, 4, 5]
    # value = [3, 4, 5, 6]
    # N = len(weight)
    # capacity = 8
    # dp = [[0] * (capacity + 1) for _ in range(N + 1)]  # dp[i][j]表示容量为j的背包放置前i个物品的最大价值和
    # for i in range(1, N + 1):                # 背包容量和物品数目都不能为0
    #     for j in range(1, capacity + 1):        # 这里顺序逆序无所谓，因为需要的数据存在上一行
    #         if j >= weight[i - 1]:
    #             dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i - 1]] + value[i - 1])
    #         else:
    #             dp[i][j] = dp[i - 1][j]   # 放不下第i个物品，就只能放到第i - 1个物品
    # print(dp[-1][-1])



