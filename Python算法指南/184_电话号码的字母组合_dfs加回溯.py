import copy


class Solution(object):
    def letterCombinations2(self, digits):
        chr = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        res = []
        for i in range(0, len(digits)):
            num = int(digits[i])
            tmp = []
            for j in range(0, len(chr[num])):
                if len(res):
                    for k in range(0, len(res)):
                        tmp.append(res[k] + chr[num][j])
                else:
                    tmp.append(str(chr[num][j]))
            res = copy.copy(tmp)
        return res

    def letterCombinations(self, digits, ans, results, start):
        jianpan = ["", " ", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        if len(ans) == len(digits):
            results.append(list(ans))
            return
        digitsList = list(map(int, digits))
        num = digitsList[start]
        size = len(jianpan[num])
        for i in range(size):
            ans.append(jianpan[num][i])
            self.letterCombinations(digits, ans, results, start + 1)
            ans.remove(jianpan[num][i])


if __name__ == '__main__':
    temp = Solution()
    string1 = "3"
    ans = []
    results = []
    print(("输入：" + string1))
    temp.letterCombinations(string1, ans, results, 0)
    for x in results:
        print(x)

