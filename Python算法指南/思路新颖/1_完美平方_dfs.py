import math
class Solution:
    def numSquares(self, n):
        ans, result, final = [], [], []
        k = int(math.sqrt(n))
        self.dfs(k, 0, ans, result)
        min_len = 65536
        for x in result:
            if len(x) < min_len:
                min_len = len(x)
                final = x
        return final

    def dfs(self, k, sum, ans, result):
        if sum == n:
            result.append(ans[:])
            return
        elif sum > n:
            return
        if len(ans) > 10:
            return
        for i in range(k):
            sum += i * i
            if sum > n:
                return
            ans.append(sum)
            self.dfs(n, sum, ans, result)
            ans.pop()
            sum -= i * i

if __name__ == '__main__':
    n = 13
    solution = Solution()
    print(solution.numSquares(n))
