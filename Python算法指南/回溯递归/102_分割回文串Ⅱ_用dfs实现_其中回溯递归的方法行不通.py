class Solution:
    def partition(self, s):
        results = []
        self.dfs(s, [], results)
        return results

    def dfs1(self, s, stringlist, results):  #stringlist为一次递归的结果, results为多次递归的结果
        if len(s) == 0:
            results.append(stringlist)
            return
        for i in range(1, len(s) + 1):
            prefix = s[:i]
            if self.is_palindrome(prefix):
                self.dfs(s[i:], stringlist + [prefix], results)  # 这样做的好处是不用回溯

    def dfs1(self, s, stringlist, results):
        if len(s) == 0:
            results.append(stringlist)
            return
        for i in range(1, len(s) + 1):
            tempStr = s[: i]
            if self.is_palindrome(tempStr):
                stringlist.append(str(tempStr))
                self.dfs(s[i:], stringlist, results)  # 采取这种回溯的方法居然不行
                stringlist.pop()

    def is_palindrome(self, s):
        return s == s[::-1]
if __name__ == '__main__':
    s = "aab"
    print("字符串是：", s)
    solution = Solution()
    print("结果是：", solution.partition(s))

