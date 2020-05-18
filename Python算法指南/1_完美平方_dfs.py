import math
class Solution:
    def numSquares2(self, n):
        while n % 4 == 0:  # 去除4的倍数
            n //= 4
        if n % 8 == 7:
            return 4
        for i in range(int(n ** 0.5) + 1): # 保证本身可以取到
            temp = i * i
            temp2 = n - i * i
            if int(temp2 ** 0.5) ** 2 == temp2:  # 判断temp2是否是完全平方
                return 1 + (0 if temp == n or temp2 == 0 else 1) # 如果其中有一个正好等于n，那么就返回1，否则返回2
        return 3

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
        if sum > n:
            return
        if len(ans) > 4: # 因为可以取重复的数，所以需要限制长度
            return
        for i in range(k):
            sum += i * i
            ans.append(i)
            self.dfs(n, sum, ans, result)
            ans.pop()
            sum -= i * i

if __name__ == '__main__':
    n = 13
    solution = Solution()
    print(solution.numSquares2(n))
