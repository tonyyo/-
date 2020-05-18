from itertools import combinations, permutations

words = ["area", "lead", "wall"]
results = list(combinations(words, 2)) # 在数组中取两个数的所有可能情况，不分先后
print(results)
results2 = list(permutations(words, 2)) # 在数组中取两个数的所有排列情况，分先后
print(results2)