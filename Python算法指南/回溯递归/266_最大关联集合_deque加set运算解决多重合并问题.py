import collections


class Solution:
    def maximumAssociationSet1(self, ListA, ListB):
        fa = list(range(0, 5009))
        cnt = [1] * 5009
        strlist = [""]

        def gf(u):
            if fa[u] != u:
                fa[u] = gf(fa[u])
            return fa[u]

        dict = {}
        tot = 0
        for i in range(0, len(ListA)):
            a, b = 0, 0
            if ListA[i] not in dict:
                tot += 1
                dict[ListA[i]] = tot
                strlist.append(ListA[i])
            a = dict[ListA[i]]
            if ListB[i] not in dict:
                tot += 1
                dict[ListB[i]] = tot
                strlist.append(ListB[i])
            b = dict[ListB[i]]
            x, y = gf(a), gf(b)
            if x != y:
                fa[y] = x
                cnt[x] += cnt[y]
        ans = []
        k, flag = 0, 0
        for i in range(0, 5000):
            if k < cnt[gf(i)]:
                k = cnt[gf(i)]
                flag = gf(i)
        for i in range(0, 5000):
            if gf(i) == flag:
                ans.append(strlist[i])
        return ans

    def maximumAssociationSet(self, ListA, ListB):
        size = len(ListA)
        result = []
        merge = [[""] * 2 for _ in range(size)]
        queue = collections.deque()
        for i in range(size):
            merge[i][0], merge[i][1] = ListA[i], ListB[i]
            queue.append(merge[i])
        while not self.NoRepeat(queue):
            first, sec = queue.popleft(), queue.popleft()
            if set(first) & set(sec):
                queue.append(list(set(first) | set(sec)))
            else:
                queue.append(first)
                queue.append(sec)
        for i in range(len(queue)):
            result.append(queue[i])
        for i in range(len(result)):
            result[i].sort()
        return result

    def NoRepeat(self, queue):
        for i in range(len(queue)):
            for j in range(i + 1, len(queue)):
                if set(queue[i]) & set(queue[j]):
                    return False
        return True


if __name__ == '__main__':
    ListA = ["a", "b", "d", "e", "f"]
    ListB = ["b", "c", "e", "g", "g"]
    ListC = ["abc", "abc", "abc"]
    ListD = ["bcd", "acd", "def"]
    solution = Solution()
    print("最大关联集合是：", solution.maximumAssociationSet(ListA, ListB))
