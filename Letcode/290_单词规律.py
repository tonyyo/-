class Solution():
    def wordPattern(self, pattern, str):
        map = {}
        strList = str.split(" ")
        print(strList)
        if len(pattern) != len(strList):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in map:
                if strList[i] not in map.values():
                    map[pattern[i]] = strList[i]
                else:    # 如果这个value在hash表中存在过，那么就应经不满足pattern了，因为既然key不同，value也应该不同。
                    return False
            else:
                if strList[i] != map[pattern[i]]:
                    return False
        return True
if __name__ == '__main__':
    solution = Solution()
    pattern = "abba"
    Str = "dog dog dog dog"
    print(solution.wordPattern(pattern, Str))
