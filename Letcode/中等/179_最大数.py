class LargerNumKey(str):
    def __lt__(x, y):
        return x + y > y + x # 两个字符串的大小取决于看谁在前面字符串更大

class Solution:
    def largestNumber(self, nums: [int]) -> str:
        strNums = list(map(str, nums))
        strNums = sorted(strNums, key=LargerNumKey)
        return "".join(strNums) if strNums[0] != '0' else '0'
