while True:
    List = input().strip().split(";")
    if List == []:
        break
    x, y = 0, 0
    for s in List:
        if len(s) > 3 or len(s) < 2:
            continue
        if s[0] not in ['A', 'D', 'W', 'S']:
            continue
        if not s[1:].isdigit():
            continue
        if s[0] == 'A':
            x -= int(s[1:])
        elif s[0] == 'D':
            x += int(s[1:])
        elif s[0] == 'W':
            y += int(s[1:])
        else:
            y -= int(s[1:])
    print(str(x) + ',' + str(y))
