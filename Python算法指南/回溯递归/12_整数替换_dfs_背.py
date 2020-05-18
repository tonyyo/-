class Solution:
    def integeReplacement(self, n):
        ans = []
        temp = [n]
        self.dfs(n, temp, ans)
        return ans

    def dfs(self, n, temp, ans):  # temp存储沿途路径点，ans存储所有可能情况
        if n == 1:
            if len(ans) == 0:
                ans.append(temp[:])  # 只赋予值，如果没有后面的[:], 将指向同一个地址
            else:
                tempList = ans.pop()
                ans.append(temp[:] if len(temp) < len(tempList) else tempList)
            return
        if n % 2 == 0:
            temp.append(n // 2)
            self.dfs(n // 2, temp, ans)  # 一种情况，不存在回溯
        else:
            for x in [-1, 1]:
                temp.append(n + x)
                self.dfs(n + x, temp, ans)
                temp.pop()  # 两种情况， 需要回溯


if __name__ == '__main__':
    solution = Solution()
    print("输出:", solution.integeReplacement(18))
