# 参数words是一个独特的单词列表
# 返回所有不同索引的组合
class Solution:
    def palindromePairs2(self, words):
        if not words:
            return []
        table = dict()
        for idx, word in enumerate(words):
            table[word] = idx
        ans = []
        for idx, word in enumerate(words):
            size = len(word)
            for i in range(size + 1):
                leftSub = word[:i]
                rightSub = word[i:]
                if self.isPalindrome(leftSub):
                    reversedRight = rightSub[::-1]
                    if reversedRight in table and table[reversedRight] != idx:
                        ans.append([table[reversedRight], idx])
                if len(rightSub) > 0 and self.isPalindrome(rightSub):
                    reversedLeft = leftSub[::-1]
                    if reversedLeft in table and table[reversedLeft] != idx:
                        ans.append([idx, table[reversedLeft]])
        return ans

    def isPalindrome(self, word):
        if not word:
            return True
        left = 0
        right = len(word) - 1
        while left <= right:
            if word[left] != word[right]:
                return False
            left += 1
            right -= 1
        return True

    def palindromePairs(self, words):
        size = len(words)
        result = []
        for i in range(size):
            for j in range(size):
                if i != j:
                    tempStr = words[i] + words[j]
                    if self.isPalindrome(tempStr):
                        result.append([i, j])
        return result

# 主函数
if __name__ == "__main__":
    words = ["bat", "tab", "cat"]
    # 创建对象
    solution = Solution()
    print("输入的数组是 ", words)
    print("输出的结果是：", solution.palindromePairs(words))
