if __name__ == '__main__':
    string ="123456789"
    N = len(string)
    a = 1
    b = 2 if int(string[:2]) <= 26 else 1
    for i in range(2, N):
        if int(string[i - 1 : i + 1]) <= 26:  # 末尾两数不能大于26
            a, b = b, a + b
        else:
            a, b = b, a  # 大于26， f(n) = f(n - 1)
    print(b)
