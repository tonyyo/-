if __name__ == '__main__':
    x, y = 2, 3
    x = x ^ y
    y = x ^ y
    x = x ^ y
    print(x)
    print(y)

