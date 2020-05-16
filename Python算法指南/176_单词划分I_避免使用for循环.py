class Solution:
    def wordBreak(self, s, dict):
        i = 1
        while(len(s) >= 0): # 因为s长度可变, 所以应避免使用for循环
            if s[0: i] in dict:
                s = s[i:]
                i = 1  # 重新初始化
            if s == "":
                return True
            i += 1
        return False


if __name__ == '__main__':
    temp = Solution()
    string1 = "helloworldhahahhelloworld"
    List = ["hello", "world", "hahah"]
    print(("输入：" + string1 + "  " + str(List)))
    print(("输出：" + str(temp.wordBreak(string1, List))))
