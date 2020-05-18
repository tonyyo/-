class Solution:
    def numDecodings1(self, s):
        if s == "" or s[0] == '0':
            return 0
        dp = [1, 1]
        for i in range(2, len(s) + 1):
            if 10 <= int(s[i - 2: i]) <= 26 and s[i - 1] != '0':
                dp.append(dp[i - 1] + dp[i - 2])
            elif int(s[i - 2: i]) == 10 or int(s[i - 2: i]) == 20:
                dp.append(dp[i - 2])
            elif s[i - 1] != '0':
                dp.append(dp[i - 1])
            else:
                return 0
        return dp[len(s)]

    def numDecodings(self, s):
        ans, result = [], []
        self.dfs(s, ans, result)
        return len(result)

    def dfs(self, s, ans, result):
        if s == "":
            result.append(ans[:])
            return
        for i in range(1, 3):
            if i > len(s):
                continue
            tempStr = s[: i]
            if int(tempStr) > 26 or int(tempStr) <= 0:
                continue
            ans.append(tempStr)
            self.dfs(s[i:], ans, result)
            ans.pop()


if __name__ == '__main__':
    temp = Solution()
    string1 = "1"
    string2 = "23"
    print(("输入：" + string1))
    print(("输出：" + str(temp.numDecodings(string1))))
    print(("输入：" + string2))
    print(("输出：" + str(temp.numDecodings(string2))))
