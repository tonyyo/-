class Solution:
    def canWin(self, s, count, flags):
        if not s.__contains__("++"):
            if  count % 2 == 1:
                return True
            else:
                return False
        for i in range(len(s) - 1):
            tempS = s
            if s[i: i + 2] == "++":  # 直到找到为止
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