class Solution:
    def strStr2(self, source, target):
        if source is None or target is None:
            return -1
        len_s = len(source)
        len_t = len(target)
        for i in range(len_s - len_t + 1):
            j = 0
            while (j < len_t):
                if source[i + j] != target[j]:
                    break
                j += 1
            if j == len_t:
                return i
        return -1

    def strStr(self, source, target):
        lenSource = len(source)
        lenTarget = len(source)
        for i in range(lenSource):
            tempStr = source[i: i + lenTarget]
            if tempStr == target:
                return i
        return -1


if __name__ == '__main__':
    temp = Solution()
    string1 = "abcd"
    string2 = "cd"
    print(("输入：" + string1 + "  " + string2))
    print(("输出：" + str(temp.strStr(string1, string2))))
