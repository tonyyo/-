class Solution:
    def anagrams2(self, strs):
        dict = {}
        for word in strs:
            sortedword = ''.join(sorted(word))
            dict[sortedword] = [word] if sortedword not in dict else dict[sortedword] + [word]
        res = []
        for item in dict:
            if len(dict[item]) >= 2:
                res += dict[item]
        return res

    def anagrams(self, strs):
        dict = []
        dict.append(sorted(strs[0]))
        ans = []
        for x in strs:
            sort_x = sorted(x)
            if sort_x in dict:
               ans.append(x)
            dict.append(sort_x)
        return ans


if __name__ == '__main__':
    temp = Solution()
    List1 = ["abcd", "bcad", "dabc", "etc"]
    List2 = ["mkji", "ijkm", "kjim", "imjk"]
    print(("输入：" + str(List1)))
    print(("输出：" + str(temp.anagrams(List1))))
    print(("输入：" + str(List2)))
    print(("输出：" + str(temp.anagrams(List2))))
