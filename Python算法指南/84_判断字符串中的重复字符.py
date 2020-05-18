class Solution:
    def isUnique(self, str):
        if len(str) > len(set(str)):
            return False
        else:
            return True
if __name__ == "__main__":
    str = "abc"
    solution = Solution()
    print("输入的字符串是：", str)
    print("输出的结果是：", solution.isUnique(str))