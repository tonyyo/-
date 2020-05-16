class Solution:
    def lengthOfLastWord(self, s):
        return len(s.strip().split(' ')[-1])
if __name__ == '__main__':
    temp = Solution()
    string1 = "hello world"
    print(("输入："+string1))
    print(("输出："+str(temp.lengthOfLastWord(string1))))