class Solution:
    def addBinary(self, a, b):
        str = "".join(a)
        str2 = "".join(b)
        sum = int(str, 2) + int(str2, 2)
        print(bin(sum)[2:])

    def addBinary2(self, a, b):
        indexa = len(a) - 1
        indexb = len(b) - 1
        carry = 0
        sum = ""
        while indexa >= 0 or indexb >= 0:
            x = int(a[indexa]) if indexa >= 0 else 0
            y = int(a[indexb]) if indexb >= 0 else 0  # 这样已经默认ａ和ｂ是字符串，不然时没办法直接对数字进行索引的
            if (x + y + carry) % 2 == 0:  # 加上当前进位后的值为多少
                sum = "0" + sum
            else:
                sum = "1" + sum
            carry = (x + y + carry) / 2  # 进位留到下一次相加时使用
            indexa -= 1
            indexb -= 1  # 使用while循环两个步骤不能忘
        if carry == 1: # 循环结束, 如果还有进位, 则要在左边补充一位
            sum = "1" + sum
        return sum

if __name__ == '__main__':
    temp = Solution()
    string1 = "1"
    string2 = "10"
    print(("输入："+string1+"+"+string2))
    print(("输出："+str(temp.addBinary(string1,string2))))

# class Solution:
#     def addBinary(self, a, b):
#         indexa = len(a) - 1
#         indexb = len(b) - 1
#         carry = 0
#         sum = ""
#         while indexa >= 0 or indexb >= 0:
#             x = int(a[indexa]) if indexa >= 0 else 0
#             y = int(b[indexb]) if indexb >= 0 else 0
#             if (x + y + carry) % 2 == 0:
#                 sum = '0' + sum
#             else:
#                 sum = '1' + sum
#             carry = (x + y + carry) / 2  # 进位
#             indexa, indexb = indexa - 1, indexb - 1
#         if carry == 1: #最后一个进位
#             sum = '1' + sum
#         return sum