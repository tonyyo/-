class Solution:  #https://blog.csdn.net/baodream/article/details/80417695
    def minDistance(self, word1, word2):
        n, m = len(word1), len(word2)
        f = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            f[i][0] = i  # 当B子串为0时，B子串要转化为A子串，要插入i次
        for j in range(m + 1):
            f[0][j] = j   # 当A子串为0时，A子串要转化为B子串，要插入j次
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]: # 因为循环从1开始
                    # f[i][j] = min(f[i - 1][j - 1], f[i - 1][j] + 1, f[i][j - 1] + 1)
                    f[i][j] = f[i - 1][j - 1] # 两子串同时加上一个字符，无需修改
                else:
                    f[i][j] = min(f[i - 1][j - 1], f[i - 1][j], f[i][j - 1]) + 1
        return f[n][m]
if __name__ == '__main__':
    temp = Solution()
    string1 = "hello"
    string2 = "world"
    print(("输入："+string1+"  "+string2))
    print(("输出："+str(temp.minDistance(string1,string2))))