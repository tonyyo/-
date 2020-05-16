class Solution:
    def numofplan1(self, n, a, k):
        ji = [0] * 1000010
        cnt = [0] * 1000010
        # 将所有可能两数之积小于等于k的值存储起来, 并计数有多少个
        for i in range(n):
            for j in range(i + 1, n):
                if(a[i] * a[j] <= k):
                    ji[a[i] * a[j]] += 1
        # 将所有小于等于k的值存储起来, 用来去重
        for i in range(n):
            if a[i] <= k:
                cnt[a[i]] += 1
        # 整理两个列表, 符合小于等于这个条件
        for i in range(1, k + 1):  # k必须要能取到
            ji[i] += ji[i -1]
            cnt[i] += cnt[i - 1]
        # 将所有的情况统计并去重
        ans = 0
        for i in range(n):
            for j in range(i + 1, n): # 对同一列表进行便利时, 防止重复
                if(a[i] * a[j] > k):
                    continue
                res = k // (a[i] * a[j])
                ans += ji[res]  # 所有可能出现的情况
                if a[i] <= res:
                    ans -= cnt[res // a[i]]  # 减去a[i]的重复
                    if a[i] <= res // a[i]:  # 如果a[i]也在其上, 那么就重复减了一次, 需要加回来
                        ans += 1
                if a[j] <= res:
                    ans -= cnt[res // a[j]]
                    if a[j] <= res // a[j]:
                        ans += 1
                if a[i] * a[j] <= res:
                    ans += 1
        return ans // 6

    def numofplan(self, n, a, k):
        ans, result, start = [], [], 0
        self.dfs(n, a, k, start, ans, result)
        print(result)
        return len(result)

    def dfs(self, n, a, k, start, ans, result):
        if len(ans) == 4:
            if self.chengji(ans) <= k:
                result.append(ans[:])
                return
            else:
                return
        elif len(ans) > 4:
            return
        elif start == n - 1 and len(ans) < 4:
            return
        for i in range(start, n):
            ans.append(a[i])
            self.dfs(n, a, k, i + 1, ans, result)
            ans.pop()

    def chengji(self, ans):
        ji = 1
        for x in ans:
            ji *= x
        return ji

if __name__ == '__main__':
    n = 5
    a = [1, 1, 1, 2, 2]
    k = 3
    solution = Solution()
    print(solution.numofplan(n,a,k))