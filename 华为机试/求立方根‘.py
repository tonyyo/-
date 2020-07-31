def cubeRoot(N):
    left, right, neg = 0, abs(N), False
    if N < 0:
        neg = True
    interval = 0.001  # 取后两位，取后一位的话还是会出现四舍五入的情况
    while right - left > interval:
        mid = (left + right) / 2
        if mid * mid * mid < N:
            left = mid
        else:
            right = mid
    left = round(left, 1)
    print(left if not neg else -left)

while True:
    try:
        N = int(input())
        cubeRoot(N)
    except:
        break
