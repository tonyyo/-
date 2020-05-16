class Solution:
    def find(self, x, f):
        if x != f[x]:
            f[x] = self.find(f[x], f)
        return f[x]

    def setUnion1(self, sets):
        f = {}
        for s in sets:
            first = s[0]
            for x in s:
                if not x in f:
                    f[x] = first
                else:
                    fFirst = self.find(first, f)
                    fx = self.find(x, f)
                    if fx != fFirst:
                        f[fx] = fFirst
        for s in sets:
            for x in s:
                self.find(x, f)
        hashSet = {}
        n = 0
        for val in f.values():
            if not val in hashSet:
                n += 1
                hashSet[val] = val
        return n

    def setUnion(self, sets):
        rowNum = len(sets)
        visited = [False for _ in range(rowNum)]
        sets = sorted(sets, key=lambda x: (x[0], x[-1]))
        result = []
        for i in range(rowNum):
            for j in range(i + 1, rowNum):
                if set(sets[i]) & set(sets[j]):
                    result.append(list(set(sets[i]) | set(sets[j])))
                    visited[i], visited[j] = True, True
            if not visited[i]:
                result.append(sets[i])
        return result


if __name__ == '__main__':
    list1 = [[1, 2, 3], [3, 9, 7], [4, 5, 10]]
    print("list1是：", list1)
    solution = Solution()
    print("合并后的集合是：", solution.setUnion(list1))
    list2 = [[1], [1, 2, 3], [4], [8, 7, 4, 5]]
    print("lis2t是：", list2)
    print("合并后的集合是：", solution.setUnion(list2))
