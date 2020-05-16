class Solution:
    def findRepeatedDna(self, s):
        length = len(s)
        dict = {}
        ans = []
        for i in range(length - 9):
            temp = s[i: i + 10]
            if temp not in dict:
                dict[temp] = 1
            else:
                dict[temp] += 1

        for key, val in dict.items(): # 遍历字典要用items
            if val > 1:
                ans.append(key)
        return ans
if __name__ == '__main__':
    s = "AAAAACCCCCAAAAACCCCCAAAAAGGGTTT"
    solution = Solution()
    print(solution.findRepeatedDna(s))

# class Solution:
#     def findRepeatedDna(self, s):
#         dict = {}
#         for i in range(len(s) - 9):  # 因为找长度为10的字符串序列
#             key = s[i: i + 10]
#             if key not in dict:
#                 dict[key] = 1   # 存在性问题初始化
#             else:
#                 dict[key] += 1
#         result = []
#         for element in dict:
#             if dict[element] > 1:
#                 result.append(element)
#         return result
