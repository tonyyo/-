class Solution():
    def wordPattern(self, pattern, str):
        map = dict()
        split_arr = str.split(" ")
        if len(split_arr) != len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in map:
                if split_arr[i] in map.values():
                    return False
                map[pattern[i]] = split_arr[i]
            else:
                if map[pattern[i]] != split_arr[i]:
                    return False
        return True

if __name__ == '__main__':
    solution = Solution()
    pattern = "abba"
    Str = "dog dog dog dog"
    print(solution.wordPattern(pattern, Str))
