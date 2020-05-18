class Solution:
    def canWin(self, s, count):
        flag = False
        if not s.__contains__("++"):
            if  count % 2 == 1:
                return True
            else:
                return False
        for i in range(len(s) - 1):
            tempS = s
            if s[i: i + 2] == "++":
                s = s[0: i] + "--" + s[i + 2:] # 替换字符串操作
                flag = self.canWin(s, count + 1)
                if flag == True: # 回溯 return 布尔值关键操作
                    return True
                s = tempS
        return flag

#主函数
if __name__ == '__main__':
    s = "+++++"
    s2 = "++++"
    print("s是：", s)
    solution = Solution()
    flags = []
    print(solution.canWin(s, 0))
    print("s2是：", s2)
    print(solution.canWin(s2, 0))