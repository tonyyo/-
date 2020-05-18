List = []
while True:
    try:
        s = input()
        if s == '':
            raise IOError
        List.append(s.strip().split('~'))
    except:
        break
flag = [0 for _ in range(7)]
for L in List:
    try:
        ip = list(map(int, L[0].strip().split('.')))
        ym = list(map(int, L[1].strip().split('.')))
    except:
        flag[5] += 1 # 格式不对，那么属于错误IP地址
        continue

    ym_s = ''
    for x in ym:
        if x == 0:
            ym_s += '0' * 8
        else:
            ym_s += bin(x)[2:]
    if ym_s.index('0') + ym_s[::-1].index('1') != 32:
        flag[5] += 1  # 掩码不符合格式，属于错误IP地址
        continue

    if ip[0] in range(1, 127):
        if ip[0] == 10: # 私有地址
            flag[6] += 1
        flag[0] += 1
    elif ip[0] in range(128, 192):
        if ip[0] == 172: # 私有地址
            flag[6] += 1
        flag[1] += 1
    elif ip[0] in range(192, 224):
        if ip[0] == 192 and ip[1] == 168: # 私有地址
            flag[6] += 1
        flag[2] += 1
    elif ip[0] in range(224, 240):
        flag[3] += 1
    elif ip[0] in range(240, 256):
        flag[4] += 1
    elif ip[0] == 0:
        continue
    else:
        flag[5] += 1

strFlag = [str(x) for x in flag]
print(' '.join(strFlag).strip())