class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        self.ans, tmp= [], []
        self.dfs(candidates, target, 0, tmp)
        return self.ans
    def dfs(self, can, target, p, tmp):
        if sum(tmp) == target:
            tmp = tmp[:]
            tmp = sorted(tmp)
            if tmp not in self.ans: # 因为有重复数字，所以可能会存在重复情况。
                self.ans.append(tmp)
            return
        if p == len(can): # 取到了末尾数必须返回
            return
        for i in range(p, len(can)): # 从p开始保证只取一次
            tmp.append(can[i])
            self.dfs(can, target, p + 1, tmp)
            tmp.pop()
        return
#主函数
if __name__ == '__main__':
    candidates = [10, 1, 6, 7, 2, 1, 5]
    target = 8
    print("候选数字：", candidates)
    print("目标数字：", target)
    solution = Solution()
    print("结果是：", solution.combinationSum2(candidates, target))