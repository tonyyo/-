import math

if __name__ == '__main__':
    point = 0.0000000001
    left, right = 1.4, 1.5
    while right - left > point: # 原来的二分法是right - left > 1
        mid = (left + right) / 2
        if mid * mid > 2:
            right = mid
        else:
            left = mid
    string = str(mid)
    print(string[:12])
    print(mid)
    print(math.sqrt(2))