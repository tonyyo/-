class Solution:
    def isPalindrome(self, s):
        start, end = 0, len(s) - 1
        while start < end:
            while start < end and not s[start].isalpha() and not s[start].isdigit():
                start += 1
            while start < end and not s[end].isalpha() and not s[end].isdigit():
                end -= 1
            if start < end and s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1
        return True
if __name__ == '__main__':
    temp = Solution()
    string1 = "a blame malba"
    string2 = "a pencil"
    print(("输入："+string1))
    print(("输出："+str(temp.isPalindrome(string1))))
    print(("输入："+string2))
    print(("输出："+str(temp.isPalindrome(string2))))