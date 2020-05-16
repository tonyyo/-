class Solution:
    def concatenetedString(self, s1, s2):
        result = [a for a in s1 if a not in s2] + [b for b in s2 if b not in s1]
        return ''.join(result)

    def concatenetedString(self, s1, s2):
        listS1 = list(s1)
        listS2 = list(s2)
        # return (set(listS2) | set(listS1)) - (set(listS2) & set(listS1))
        return ''.join([a for a in s1 if a not in s2] + [b for b in s2 if b not in s1])
if __name__ == "__main__":
    s1 = "aacdb"
    s2 = "gafd"
    solution = Solution()
    print("输入的两个字符串是：s1=", s1, "s2=", s2)
    print("计算的结果是：", solution.concatenetedString(s1, s2))