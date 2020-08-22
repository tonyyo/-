def splits(arr):
    N = len(arr)
    low, mid, high = 0, 0, N - 1 # 分别指向三个区域的第一个位置
    while mid <= high:      # 这里必须加上等于
        cur = arr[mid]
        if cur < 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
            # 因为mid是和low一起从左边遍历过来的, low指向的元素的值其实是0, 所以交换起来正好, 然后两者都要+1
        elif cur == 0:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1  # 这里mid=不能+1, 因为从高位交换过去的数要重新进行比较

arr = [0, 1, -1, 2, -2, 0, 3]
splits(arr)
print(arr)