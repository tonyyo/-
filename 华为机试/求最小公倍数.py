while True:
    try:
        m, n = map(int, input().strip().split())
        product = m * n
        while n != 0:
            m, n = n, m % n
        print(product // m)
    except:
        break
