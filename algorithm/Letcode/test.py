if __name__ == '__main__':
    n = 4333
    strn = str(n)
    List = list(map(int, strn))
    s = "".join(str(x) for x in List)
    print(s)
