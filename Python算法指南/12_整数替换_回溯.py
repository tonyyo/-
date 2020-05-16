class Solution:
    def integeReplacement(self, n):
        ans, result, final = [], [], []
        self.dfs(n, ans, result)
        min_len = 65536
        for i in range(len(result)):
            if len(result[i]) < min_len:
                min_len = min(min_len, len(result[i]))
                final = result[i]
        return final


    def dfs(self, n, ans, result):
        if n == 1:
            ans.append(1)
            result.append(ans[:])
            return
        if n % 2 == 0:
            ans.append(n)
            self.dfs(n // 2, ans, result)
            ans.pop()
        else:
            for i in range(2):
                if i == 1:
                    ans.append(n)
                    self.dfs(n + 1, ans, result)
                    ans.pop()
                else:
                    ans.append(n)
                    self.dfs(n - 1, ans, result)
                    ans.pop()

if __name__ == '__main__':
    solution = Solution()
    print("输出:", solution.integeReplacement(18))