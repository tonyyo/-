class Solution:
    def multiply2(self, num1, num2):
        l1, l2 = len(num1), len(num2)
        l3 = l1 + l2
        res = [0 for i in range(l3)]
        for i in range(l1 - 1, -1, -1):
            carry = 0
            for j in range(l2 - 1, -1, -1):
                res[i + j + 1] += carry + int(num1[i]) * int(num2[j])
                carry = res[i + j + 1] // 10
                res[i + j + 1] %= 10
            res[i] = carry
        i = 0
        while i < l3 and res[i] == 0:
            i += 1
        res = res[i:]
        return '0' if not res else ''.join(str(i) for i in res)

if __name__ == '__main__':
    num1 = '123'
    num2 = '45'
    print("初始整数：", num1, num2)
    solution = Solution()
    print("结果：", solution.multiply(num1, num2))