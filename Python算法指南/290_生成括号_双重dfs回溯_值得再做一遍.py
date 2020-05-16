class Solution:
    def helpler(self, l, r, item, res):
        if r < l:
            return
        if l == 0 and r == 0:
            res.append(item)
        if l > 0:
            self.helpler(l - 1, r, item + '(', res)
        if r > 0:
            self.helpler(l, r - 1, item + ')', res)

    def generateParenthesis1(self, n):
        if n == 0:
            return []
        res = []
        self.helpler(n, n, '', res)
        return res

    def generateParenthesis(self, n):
        kuohaos = []
        ans, result, final = [], [], []
        for i in range(n):
            kuohaos.append('(')
            kuohaos.append(')')
        self.dfs(kuohaos, 0, result)
        for x in result:
            if self.isVaild(x):
                final.append(x)
        return final

    def isVaild(self, string):
        stack = []
        for x in string:
            if x == ')':
                if len(stack) == 0:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(x)
        if len(stack) == 0:
            return True
        else:
            return False


    def dfs(self, kuohaos, start, result):
        if start == len(kuohaos):
            temp = kuohaos[:]
            string = ""
            for x in temp:
                string += x
            if string not in result:
                result.append(string)

        for i in range(start, len(kuohaos)):
            kuohaos[start], kuohaos[i] = kuohaos[i], kuohaos[start]
            self.dfs(kuohaos, start + 1, result)
            kuohaos[start], kuohaos[i] = kuohaos[i], kuohaos[start]


if __name__ == '__main__':
    temp = Solution()
    nums1 = 3
    nums2 = 2
    print(("输入：" + str(nums1)))
    print(("输出：" + str(temp.generateParenthesis(nums1))))
    print(("输入：" + str(nums2)))
    print(("输出：" + str(temp.generateParenthesis(nums2))))
