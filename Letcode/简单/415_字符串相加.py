class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        List1, List2, carry, res = list(num1), list(num2), 0, ""
        while List1 or List2 or carry != 0: # carry不等于0能够将最后的进位补在前面
            a = int(List1.pop()) if List1 else 0
            b = int(List2.pop()) if List2 else 0
            v = (a + b + carry) % 10
            carry = (a + b + carry) // 10
            res = str(v) + res
        return res


