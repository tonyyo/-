class Solution:
    def longestPalindrome(self, s):
        if not s:
            return ""
        longest = ""
        for middle in range(len(s)):
            sub = self.find_palindrome_from(s, middle, middle)
            if len(sub) > len(longest):
                longest = sub
            sub = self.find_palindrome_from(s, middle, middle + 1)
            if len(sub) > len(longest):
                longest = sub
        return longest

    def find_palindrome_from(self, string, left, right):
        while left >= 0 and right < len(string) and string[left] == string[right]:
            left -= 1
            right += 1
        return string[left + 1:right]

    def longestPalindrome(self, s):
        length = len(s)
        ans = {}
        flag = 0
        for i in range(length, 0, -1):
            for j in range(length - i + 1):
                tempStr = s[j: j + i]
                if tempStr == tempStr[::-1]:
                    ans[tempStr] = len(tempStr)
                    flag = 1
                    break
            if flag == 1:
                break
        print(ans)
        result = ""
        length = 0
        for key in ans.keys():
            if len(key) > length:
                length = len(key)
                result = key
        return result

if __name__ == '__main__':
    temp = Solution()
    string1 = "abcdedcb"
    string2 = "qwerfdfdfg"
    print(("输入：" + string1))
    print(("输出：" + str(temp.longestPalindrome(string1))))
    print(("输入：" + string2))
    print(("输出：" + str(temp.longestPalindrome(string2))))
