class Solution:
    def lengthOfLongestSubstring(self, s):
        unique_chars = set([])
        j = 0
        n = len(s)
        longest = 0
        for i in range(n):
            while j < n and s[j] not in unique_chars:
                unique_chars.add(s[j])
                j += 1
            longest = max(longest, j - i)
            unique_chars.remove(s[i])
        return longest

    def lengthOfLongestSubstring2(self, s):
        length = len(s)
        longest = 0
        ans = []
        for i in range(1, length + 1):
            for j in range(length - i + 1):
                tempStr = s[j: j + i]
                if len(tempStr) != len(set(tempStr)):
                    continue
                else:
                    longest = max(longest, i)
                    ans.append(tempStr)
        print(ans)
        return longest


if __name__ == '__main__':
    temp = Solution()
    string1 = "abccdavf"
    print(("输入：" + string1))
    print(("输出：" + str(temp.lengthOfLongestSubstring2(string1))))
