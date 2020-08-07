def getSum(a, b):
    while b != 0:
        temp = a ^ b # 第一次是a、b两数相加，后面都是和进位值相加，temp存的是相加后的结果
        b = (a & b) << 1 # b为进位值，没有进位了就跳出循环
        a = temp
    return a
print(getSum(-1, 1))