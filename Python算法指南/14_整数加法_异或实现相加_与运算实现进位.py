class Solution:
    def aplusb(self, a, b):
        xor = a ^ b
        jinwei = (a & b) << 1
        while jinwei != 0:  # 直到进位与异或的结果与运算后结果为0
            temp = xor ^ jinwei
            jinwei = (xor & jinwei) << 1
            xor = temp
        return xor

if __name__ == '__main__':
    solution = Solution()
    print(solution.aplusb(1,3))