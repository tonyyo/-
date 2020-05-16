class Solution:
    def minWindow(self, source, target):
        if source is None:
            return ""
        targetHash = self.getTargetHash(target)
        targetUniqueChars = len(targetHash)
        matchedUniqueChars = 0
        hash = {}
        n = len(source)
        j = 0
        minLength = n + 1
        minWindowString = ""
        for i in range(n):
            while j < n and matchedUniqueChars < targetUniqueChars:
                if source[j] in targetHash:
                    hash[source[j]] = hash.get(source[j], 0) + 1
                    if hash[source[j]] == targetHash[source[j]]:
                        matchedUniqueChars += 1
                j += 1
            if j - i < minLength and matchedUniqueChars == targetUniqueChars:
                minLength = j - i
                minWindowString = source[i:j]
            if source[i] in targetHash:
                if hash[source[i]] == targetHash[source[i]]:
                    matchedUniqueChars -= 1
                hash[source[i]] -= 1
        return minWindowString

    def getTargetHash(self, target):
        hash = {}
        for c in target:
            hash[c] = hash.get(c, 0) + 1
        return hash

    def minWindow(self, source, target):
        lenSource = len(source)
        lenTarget = len(target)
        target = "".join(sorted(target))
        for i in range(lenTarget, lenSource):
            for j in range(lenSource - i + 1):
                tempStrList = source[j: j + i]
                tempStr = "".join(sorted(tempStrList))
                if tempStr.__contains__(target):
                    return "".join(tempStrList)
        return -1

if __name__ == "__main__":
    source = "ADOBECODEBANC"
    target = "ABC"
    solution = Solution()
    print("初始的字符串是：", source, "初始的目标值是：", target)
    print("符合条件的最短子串是：", solution.minWindow(source, target))
