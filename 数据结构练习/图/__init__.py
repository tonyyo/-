from collections import defaultdict

s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)
print(d)