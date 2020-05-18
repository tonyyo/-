total, row = map(int, input().split())
total //= 10   # 同倍数的缩小背包和物品的重量
w = [[0 for _ in range(4)] for _ in range(row)]
v = [[0 for _ in range(4)] for _ in range(row)]
flag = []
for i in range(row):
    x, y, z = map(int, input().split())
    x //= 10
    if z == 0:
        w[i][0] = x
        v[i][0] = x * y
    else:
        if z not in flag:
            w[z-1][1] = w[z - 1][0] + x  # 主件加第一个附件
            v[z-1][1] = v[z - 1][0] + x * y
            flag.append(z)  # 找到了第一个附件
        else:
            w[z-1][2] = w[z - 1][0] + x
            v[z-1][2] = v[z - 1][0] + x * y
            w[z-1][3] = w[z - 1][1] + x
            v[z-1][3] = v[z - 1][1] + x * y
dp = [0 for _ in range(total + 1)]  # 背包容量为j，在前i个物品中选择，能够放下且价值最大的物品价值和。
for i in range(len(w)):
    for j in range(total, -1, -1):
        for k in range(4):
            if w[i][k] <= j:
                dp[j] = max(dp[j], v[i][k] + dp[j - w[i][k]])

print(dp[total] * 10)