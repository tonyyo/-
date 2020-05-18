class Solution:
    def judgeWords(self, pattern, testStr):
        listPattern = list(pattern)
        listTestStr = testStr.split()
        lenPatter = len(listPattern)
        lenTestStr = len(listTestStr)
        if lenPatter != lenTestStr:
            return False
        for i in range(1, lenTestStr):
            if listPattern[i] == listPattern[i -1] and listTestStr[i] != listTestStr[i - 1]:
                return False
            if listPattern[i] != listPattern[i - 1] and listTestStr[i] == listTestStr[i - 1]:
                return False
        return True


if __name__ == '__main__':
    temp = Solution()
    pattern = "abba"
    testStr = "dog cat cat dog"
    print(temp.judgeWords(pattern, testStr))