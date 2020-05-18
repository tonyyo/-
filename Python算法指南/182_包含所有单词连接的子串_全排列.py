class Solution(object):
    def findSubstring(self, s, words):
        hash = {}
        res = []
        wsize = len(words[0])
        for str in words:
            if str in hash:
                hash[str] += 1
            else:
                hash[str] = 1
        for start in range(0, len(words[0])):
            slidingWindow = {}
            wCount = 0
            for i in range(start, len(s), wsize):
                word = s[i: i + wsize]
                if word in hash:
                    if word in slidingWindow:
                        slidingWindow[word] += 1
                    else:
                        slidingWindow[word] = 1
                    wCount += 1
                    while hash[word] < slidingWindow[word]:
                        pos = i - wsize * (wCount - 1)
                        removeWord = s[pos: pos + wsize]
                        print(i, removeWord)
                        slidingWindow[removeWord] -= 1
                        wCount -= 1
                else:
                    slidingWindow.clear()
                    wCount = 0
                if wCount == len(words):
                    res.append(i - wsize * (wCount - 1))
        return res

    def findSubstring2(self, s, words):
        ans = []
        self.quanpailei(words, ans, 0)
        result = []
        for x in ans:
            result.append(s.index(x))
        return result

    def quanpailei(self, words, ans, start):  # 列出可能出现的所有排列情况
        if start >= len(words):
            string = ""
            for x in words:
                string = string + x
            ans.append(string)
        for i in range(start, len(words)):
            words[i], words[start] = words[start], words[i]
            self.quanpailei(words, ans, start + 1)
            words[i], words[start] = words[start], words[i]


if __name__ == '__main__':
    temp = Solution()
    string1 = "barfoothefoobarman"
    List1 = ["foo", "bar"]
    print(("输入：" + str(string1) + "  " + str(List1)))
    print(("输出：" + str(temp.findSubstring2(string1, List1))))
