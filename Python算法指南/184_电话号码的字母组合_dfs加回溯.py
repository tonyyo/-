class Solution(object):
    def letterCombinations(self, digits: str) -> [str]:
        if len(digits) == 0:
            return []
        results = []
        self.backtrack(digits, "", results)
        return results

    def backtrack(self, digits, ans, results):  # 输入digits, 单一情况存入ans, 所有情况存入results, 回溯ans
        jianpan = ["", " ", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        if len(digits) == 0:
            results.append(ans)
            return
        num = int(digits[0])
        size = len(jianpan[num])
        for i in range(size):       # 回溯的是每一个数字对应的键位的字母
            self.backtrack(digits[1:], ans + jianpan[num][i], results)


if __name__ == '__main__':
    temp = Solution()
    string1 = "34"
    print(("输入：" + string1))
    results = temp.letterCombinations(string1)
    print(results)

