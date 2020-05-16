class Solution:
    def canPermutePalindrome(self, s):
        lookup = {}
        count = 0
        for x in s: # 遍历字符串
            if x not in lookup:
                lookup[x] = 1 # 初始化
            else:
                lookup[x] += 1
        for x in lookup.values():
            count += x % 2 # 计数奇数的个数
        return count <= 1

if __name__ == "__main__":
    s = "abbv"
    solution = Solution()
    print("输入的字符串是：s=", s)
    print("输出的结果是：", solution.canPermutePalindrome(s))
