from functools import reduce

nums = [1, 2, 3]
print(reduce(lambda x, y : x * y, nums))