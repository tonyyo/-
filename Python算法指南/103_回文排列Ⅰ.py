import collections


class Solution:
    def canPermutePalindrome(self, s):
        count = 0
        lookup = collections.Counter(s)  # 计数字符串中字符的个数， 返回以字符为key的字典
        print(lookup)
        for x in lookup.values():
            count += x % 2 # 计数奇数的个数
        return count <= 1  # 要么只有一个奇数，要么没有奇数

if __name__ == "__main__":
    s = "abbv"
    solution = Solution()
    print("输入的字符串是：s=", s)
    print("输出的结果是：", solution.canPermutePalindrome(s))
