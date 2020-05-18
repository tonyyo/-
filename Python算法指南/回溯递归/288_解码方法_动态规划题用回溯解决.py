class Solution:
    def numDecodings(self, s):
        ans, result = [], []
        self.dfs(s, ans, result)
        return result

    def dfs(self, s, ans, result):
        if s == "":
            result.append(ans[:])
            return
        for i in range(1, 3): # 回溯长度为1和长度为2的字符，因为最大为26是两位。
            if i > len(s):
                continue
            tempStr = s[: i]
            if int(tempStr) > 26 or int(tempStr) <= 0:
                return
            ans.append(tempStr)
            self.dfs(s[i:], ans, result)
            ans.pop()


if __name__ == '__main__':
    temp = Solution()
    string1 = "12345678"
    string2 = "23"
    print(("输入：" + string1))
    print(("输出：" + str(temp.numDecodings(string1))))
    print(("输入：" + string2))
    print(("输出：" + str(temp.numDecodings(string2))))
