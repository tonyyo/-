from itertools import permutations

class Solution(object):
    def findSubstring(self, s, words):
        ans = []
        List = list(permutations(words)) # 全排列的每一种情况都是用元组存储的，且记得用list强制转换
        for i in range(len(List)):
            string = ''
            for j in range(len(List[i])):
                string += List[i][j]
            ans.append(s.index(string))
        return ans


if __name__ == '__main__':
    temp = Solution()
    string1 = "barfoothefoobarman"
    List1 = ["foo", "bar"]
    print(("输入：" + str(string1) + "  " + str(List1)))
    print(("输出：" + str(temp.findSubstring(string1, List1))))
