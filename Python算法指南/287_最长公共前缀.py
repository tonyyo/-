class Solution:
    def longestCommonPrefix1(self, strs):
        if len(strs) <= 1:
            return strs[0] if len(strs) == 1 else ""
        end, minl = 0, min([len(s) for s in strs])
        while end < minl:
            for i in range(1, len(strs)):
                if strs[i][end] != strs[i - 1][end]:
                    return strs[0][:end]
            end = end + 1
        return strs[0][:end]

    def longestCommonPrefix(self, strs):
        size = len(strs)
        strs = sorted(strs, key=lambda x: len(x))
        flag = True
        result = ""
        for i in range(1,len(strs[0]) + 1):
            for j in range(1, size):
                if strs[j - 1][:i] == strs[j][:i]:
                    continue
                flag = False
            if flag:
                continue
            else:
                result = strs[0][:i - 1]
                break
        return result


if __name__ == '__main__':
    temp = Solution()
    nums1 = ["ABCD", "ABEF", "ACEF"]
    nums2 = ["BCD", "BCEF", "BEF"]
    print("输入的数组：" + "['ABCD','ABEF','ACEF']")
    print("输出：" + str(temp.longestCommonPrefix(nums1)))
    print("输入的数组：" + '["BCD", "BCEF", "BEF"]')
    print("输出：" + str(temp.longestCommonPrefix(nums2)))
