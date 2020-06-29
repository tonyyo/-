class Solution:
    def restoreIpAddresses(self, s):
        ans, result, final = [], [], []
        self.dfs(s, ans, result)
        for x in result:
            final.append('.'.join(x))
        return final

    def dfs(self, s, ans, result):
        if len(s) > 16:
            return
        if s == "":
            if len(ans) == 4:
                if ans not in result:
                    result.append(ans[:])
            return
        for i in range(1, 4):
            integer = int(s[:i])
            if integer > 255 or (s[:i] != '0' and s[:i][0] == '0'):  # ip地址每段开始不能是0
                continue
            self.dfs(s[i:], ans + [s[:i]], result)

# 主函数
if __name__ == '__main__':
    solution = Solution()
    S = "010010"
    print("字符串S是：", S)
    print(solution.restoreIpAddresses(S))