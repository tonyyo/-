class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        self.ans, tmp= [], []
        self.dfs(candidates, target, tmp)
        return self.ans
    def dfs(self, can, target, tmp):
        if sum(tmp) == target:
            tmp = tmp[:]
            tmp = sorted(tmp)
            if tmp not in self.ans:
                self.ans.append(tmp)
            return
        if sum(tmp) > target:
            return
        for i in range(len(can)):
            tmp.append(can[i])
            self.dfs(can, target, tmp)
            tmp.pop()
#主函数
if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    target = 7
    print("候选数字：", candidates)
    print("目标数字：", target)
    solution = Solution()
    print("结果是：", solution.combinationSum2(candidates, target))