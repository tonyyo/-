class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry, sum = 0, ""
        M, N = len(a) - 1, len(b) - 1
        while M >=0 or N >= 0 or carry != 0: # 进位不为0
            int_a = int(a[M]) if M >= 0 else 0 # 给较短的字符串赋0
            int_b = int(b[N]) if N >= 0 else 0
            cur = (int_a + int_b + carry) % 2
            carry = (int_a + int_b + carry) // 2
            sum = str(cur) + sum
            M -= 1
            N -= 1
        return sum
