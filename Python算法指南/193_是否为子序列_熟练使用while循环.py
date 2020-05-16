class Solution(object):
    def isSubsequence2(self, s, t):
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        if i == len(s):
            return True
        else:
            return False

    def isSubsequence(self, s, t):
        sizeS = len(s)
        sizeT = len(t)
        i, j = 0, 0
        while i < sizeS and j < sizeT:
            if s[i] == s[j]:
                i += 1
            j += 1
        if i == sizeS:
            return True
        else:
            return False

if __name__ == '__main__':
    temp = Solution()
    string1 = "abc"
    string2 = "abcdefg"
    print(("输入：" + string1 + "  " + string2))
    print(("输出：" + str(temp.isSubsequence(string1, string2))))
