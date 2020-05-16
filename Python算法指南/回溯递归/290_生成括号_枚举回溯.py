from itertools import permutations


class Solution:
    def helpler(self, l, r, item, res):
        if r < l: # 放置的右括号数大于放置的左括号数，进行回溯
            return
        if r == 0 and l == 0: # 出口
            res.append(item[:])
        if l > 0:
            self.helpler(l - 1, r, item + '(', res) # 先放左括号
        if r > 0:
            self.helpler(l, r - 1, item + ')', res) # 先放右括号


    def generateParenthesis1(self, n):
        if n == 0:
            return []
        res = []
        self.helpler(n, n, '', res)
        return res

    def generateParenthesis(self, n):
        List, ans = [], []
        for i in range(n):
            List.append('(')
            List.append(')')
        possible = permutations(List)
        for x in possible:
            if self.isVaild(x) and ''.join(x) not in ans:
                ans.append(''.join(x))
        return ans

    def isVaild(self, string): # 诀窍就是遇到顺括号，就入栈，如果遇到反括号就出栈，最后如果栈为0，表示配对成功。
        stack = []
        for x in string:
            if x == ')':
                if len(stack) == 0: # 如果第一个括号就是反括号，直接返回False
                    return False
                else:
                    stack.pop()
            else:
                stack.append(x)
        if len(stack) == 0:
            return True
        else:
            return False

if __name__ == '__main__':
    temp = Solution()
    nums1 = 3
    nums2 = 2
    print(("输入：" + str(nums1)))
    print(("输出：" + str(temp.generateParenthesis1(nums1))))
    print(("输入：" + str(nums2)))
    print(("输出：" + str(temp.generateParenthesis1(nums2))))
