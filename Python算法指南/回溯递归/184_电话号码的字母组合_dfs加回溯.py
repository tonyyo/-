import copy

class Solution(object):
    def letterCombinations(self, digits, ans, results):
        jianpan = ["", " ", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        if len(digits) == 0:
            results.append(list(ans))
            return
        num = int(digits[0]) # 获得第一个
        size = len(jianpan[num])
        for i in range(size):
            ans.append(jianpan[num][i])
            self.letterCombinations(digits[1:], ans, results) # 抛弃一个
            ans.remove(jianpan[num][i])


if __name__ == '__main__':
    temp = Solution()
    string1 = "34"
    ans = []
    results = []
    print(("输入：" + string1))
    temp.letterCombinations(string1, ans, results)
    for x in results:
        print(x)

