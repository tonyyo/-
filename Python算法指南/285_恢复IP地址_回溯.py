class Solution:
    def restoreIpAddresses(self, s):
        ans, result, final = [], [], []
        self.dfs(s, ans, result)
        for x in result:
            tempStr = str(x[0])
            for i in range(1, len(x)):
                tempStr += '.' + str(x[i])
            final.append(tempStr)
        return final


    def dfs(self, s, ans, result):
        if s == "" and len(ans) == 4:
            if ans not in result:
                result.append(ans[:])
            return
        if s == "" and len(ans) < 4:
            return
        if len(ans) > 4:
            return
        for i in range(1, 4):
            integer = int(s[:i])
            if integer > 255:
                continue
            ans.append(integer)
            self.dfs(s[i:], ans, result)
            ans.pop()

# 主函数
if __name__ == '__main__':
    solution = Solution()
    S = "25525511135"
    print("字符串S是：", S)
    print(solution.restoreIpAddresses(S))