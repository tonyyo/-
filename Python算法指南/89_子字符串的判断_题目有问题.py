import collections
class Solution:
    def checkInclusion(self, s1, s2):
        len1, len2 = len(s1), len(s2)
        if not s2 or len2 < len1:
            return False
        if not s1:
            return True
        window_diff = collections.defaultdict(int)
        for c in s1:
            window_diff[c] -= 1
        for i in range(len1):
            char = s2[i]
            window_diff[char] += 1
            if window_diff[char] == 0:
                window_diff.pop(char)
        if len(window_diff) == 0:
            return True
        for i in range(len1, len2):
            char = s2[i]
            char2rm = s2[i-len1]
            window_diff[char] += 1
            window_diff[char2rm] -= 1
            if window_diff[char] == 0:
                window_diff.pop(char)
            if window_diff[char2rm] == 0:
                window_diff.pop(char2rm)
            if len(window_diff) == 0:
                return True
        return False
if __name__ == '__main__':
    temp = Solution()
    string1 = "abc"
    string2 = "dauwkbfyacb"
    print("输入："+string1+"  "+string2)
    print(("输出："+str(temp.checkInclusion(string1,string2))))