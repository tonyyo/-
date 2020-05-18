class Solution:  #https://blog.csdn.net/baodream/article/details/80417695
    def minDistance(self, word1, word2):
        n, m = len(word1), len(word2)
        f = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            f[i][0] = i
        for j in range(m + 1):
            f[0][j] = j
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    f[i][j] = min(f[i - 1][j - 1], f[i - 1][j] + 1, f[i][j - 1] + 1)
                    # equivalent to f[i][j] = f[i - 1][j - 1]
                else:
                    f[i][j] = min(f[i - 1][j - 1], f[i - 1][j], f[i][j - 1]) + 1
        return f[n][m]
if __name__ == '__main__':
    temp = Solution()
    string1 = "hello"
    string2 = "world"
    print(("输入："+string1+"  "+string2))
    print(("输出："+str(temp.minDistance(string1,string2))))