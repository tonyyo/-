from functools import reduce
class Solution:
    def subsetsWithDup(self, S):
        S.sort()
        p = [[S[x] for x in range(len(S)) if i >> x & 1] for i in range(2 ** len(S))]
        func = lambda x, y: x if y in x else x + [y]
        p = reduce(func, [[], ] + p)
        return list(reversed(p))
#主函数
if __name__ == '__main__':
    S = [1, 2, 2]
    print("S是：", S)
    solution = Solution()
    print("可能的子集是：", solution.subsetsWithDup(S))