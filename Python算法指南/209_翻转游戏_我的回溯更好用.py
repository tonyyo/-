class Solution:
    memo = {}
    def canWin2(self, s):
        if s in self.memo:
            return self.memo[s]
        for i in range(len(s) - 1):
            if s[i:i + 2] == '++':
                tmp = s[:i] + '--' + s[i + 2:]
                flag = self.canWin(tmp)
                print(flag)
                self.memo[tmp] = flag
                if not flag:
                    return True
        return False

    def canWin(self, s, count, flags):
        if not s.__contains__("++"):
            if  count % 2 == 1:
                flags.append(True)
            else:
                return
        for i in range(len(s) - 1):
            tempS = s
            if s[i: i + 2] == "++":
                s = s[0: i] + "--" + s[i + 2:]
                self.canWin(s, count + 1, flags)
                s = tempS

#主函数
if __name__ == '__main__':
    s = "++++++"
    print("s是：", s)
    solution = Solution()
    flags = []
    solution.canWin(s, 0, flags)
    print(flags)