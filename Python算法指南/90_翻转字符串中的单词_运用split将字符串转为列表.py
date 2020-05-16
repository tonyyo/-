class Solution:
    def reverseWords(self, s):
        return ' '.join(reversed(s.strip().split())) # split用空格分割, 结果用列表存储, 这样一个单词为一个整体, 就可以实现翻转
if __name__ == '__main__':
    temp = Solution()
    string1 = "hello world"
    string2 = "python learning"
    print(("输入："+string1))
    print(("输出："+temp.reverseWords(string1)))
    print(("输入："+string2))
    print(("输出："+temp.reverseWords(string2)))