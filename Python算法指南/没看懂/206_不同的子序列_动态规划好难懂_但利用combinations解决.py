import collections
from itertools import combinations


class Solution:
    def numDistinct2(self, S, T):  # https://www.jianshu.com/p/3d061dbe0c99
        dp = [[0 for j in range(len(T) + 1)] for i in range(len(S) + 1)]
        for i in range(len(S) + 1):
            dp[i][0] = 1 # 空集是所有集合的子集，所以当T为空集时，S中包含T的个数都为1
        for i in range(len(S)):
            for j in range(len(T)):
                if S[i] == T[j]:
                    dp[i + 1][j + 1] = dp[i][j + 1] + dp[i][j] # 而相等的时候还要加上S字符串减1包含T字符串减1的个数
                else:
                    dp[i + 1][j + 1] = dp[i][j + 1] # 当不等的时候毫无疑问，等于S字符串减1的包含T的个数
        for x in dp:
            print(x)
        return dp[len(S)][len(T)]

    def numDistinct(self, S, T):
        lenS = len(S)
        lenT = len(T)
        listS = list(S)
        cha = lenS - lenT
        qushu = []
        count = 0
        for i in range(lenS):
            qushu.append(i)
        possible = list(combinations(qushu, cha))
        for x in possible:
            tempListS = listS.copy()
            for y in x:
                tempListS.remove(listS[y])
            print(tempListS)
            tempS = ''.join(k for k in tempListS)
            if tempS == T:
                count += 1
        return count

#主函数
if __name__ == '__main__':
    S = "rabbbit"
    T = "rabbit"
    print("字符串S：", S)
    print("字符串T：", T)
    solution = Solution()
    print("结果：", solution.numDistinct(S, T))