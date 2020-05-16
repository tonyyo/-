class Solution:
    def restoreIpAddresses(self, s):
        ans, result, final = [], [], []
        self.dfs(s, ans, result)
        print(result)
        for x in result:
            final.append('.'.join(x))  # '任何字符'.join(字符数组)，那么将会以"任何字符"相连
        return final

    def dfs(self, s, ans, result):
        if s == "":
            if len(ans) == 4 and ans not in result:
                result.append(ans[:])
                return
            if len(ans) > 4 or len(ans) < 4:
                return

        for i in range(1, 4):
            integer = int(s[:i])
            if integer > 255: # 大于了最大值，直接返回就好
                return
            if i > len(s): # 如果剩下的字符串长度小于要截取的长度，直接返回
                return
            ans.append(s[:i])
            self.dfs(s[i:], ans, result)
            ans.pop()

# 主函数
if __name__ == '__main__':
    solution = Solution()
    S = "25525511135"
    print("字符串S是：", S)
    print(solution.restoreIpAddresses(S))