def f(vst, cur, N):
    if N == 0:
        print(" ".join(map(str,cur))) # 打印整形数组
    for i in range(1, len(vst)):
        if vst[i] or (len(cur) > 0 and i in [cur[-1] -1, cur[-1] + 1]):
            continue
        vst[i] = 1
        f(vst, cur + [i], N - 1)
        vst[i] = 0

while True:
    N = input()
    if N == "":
        break
    N = int(N)
    f([0] * (N + 1), [], N)