from collections import defaultdict


def find(List, m, n):
    hash = defaultdict(list)
    ans = 0
    for i in range(n):
        hash[List[i]].append(i) # 重复问题善于运用hash表
        if len(hash[List[i]]) >= m:
            ans += n - hash[List[i]][-1]
    print(hash)
    return ans

n, m = map(int, input().strip().split())
while True:
    string = input()
    if string == "":
        break
    List = list(map(int, string.strip().split()))
    print(List)
    print(find(List, m, n))
