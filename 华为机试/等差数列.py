while True:
    try:
        N = int(input())
        cur, Sum = 2, 2
        for _ in range(1, N):
            cur += 3
            Sum += cur
        print(Sum)
    except:
        break