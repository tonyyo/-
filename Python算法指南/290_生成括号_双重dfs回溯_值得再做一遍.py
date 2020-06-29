class Solution:
    def helpler(self, l, r, item, res):   # 当左括号数为l，右括号数为r时，生成所有有效的括号组合
        if r < l:              # 右括号的数不能少于左括号的数
            return
        if l == 0 and r == 0:
            res.append(item)
            return
        if l > 0:
            self.helpler(l - 1, r, item + '(', res)   # 先放左括号
        if r > 0:
            self.helpler(l, r - 1, item + ')', res)   # 先放右括号， 两者没有先后关系，是并列的

    def generateParenthesis(self, n):
        if n == 0:
            return []
        res = []
        self.helpler(n, n, '', res)
        return res

if __name__ == '__main__':
    temp = Solution()
    nums1 = 3
    nums2 = 2
    print(("输入：" + str(nums1)))
    print(("输出：" + str(temp.generateParenthesis(nums1))))
    print(("输入：" + str(nums2)))
    print(("输出：" + str(temp.generateParenthesis(nums2))))
