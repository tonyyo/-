import sys

if __name__ == '__main__':
    nums = [1, 1, 1, 3, 3]
    N = len(nums)
    left, right = [0] * N, [0] * N
    leftSum, rightSum = 0, 0
    leftSquareSum, rightSquareSum = 0, 0
    for i in range(N):
        leftSum += nums[i]
        leftSquareSum += nums[i] * nums[i]
        left[i] = leftSquareSum / (i + 1) - (leftSum / (i + 1)) * (leftSum / (i + 1))  # 各数平方和的均值 - 各数均值的平方

    nums = nums[::-1]
    for i in range(N):
        rightSum += nums[i]
        rightSquareSum += nums[i] * nums[i]
        right[i] = rightSquareSum / (i + 1) - (rightSum / (i + 1)) * (rightSum / (i + 1))

    k, Min = 0, sys.maxsize
    for i in range(N):
        if Min > left[i] + right[N - i - 2]:
            Min = left[i] + right[N - i - 2]
            k = i
    print(left)
    print(right)
    print(Min)
    print(k + 1)