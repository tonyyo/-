import math

if __name__ == '__main__':
    point = 0.0000000001
    left, right = 0, 2
    while right - left > point:
        mid = (left + right) / 2
        if mid * mid > 2:
            right = mid
        else:
            left = mid
    print(left)
    print(mid)
    print(right)
    print(round(mid, 10))