import collections
class Solution:
    def ladderLength(self, start, end, dict):
        dict.add(end)
        queue = collections.deque([start])
        visited = set([start])
        distance = 0
        while queue:
            distance += 1
            for i in range(len(queue)):
                word = queue.popleft()
                if word == end:
                    return distance
                for next_word in self.get_next_words(word):
                    if next_word not in dict or next_word in visited:
                        continue
                    queue.append(next_word)
                    visited.add(next_word)
        return 0
    def get_next_words(self, word): # 返回和word只相差一个单词的所有组合
        words = []
        for i in range(len(word)):
            left, right = word[:i], word[i + 1:]
            for char in 'abcdefghijklmnopqrstuvwxyz':
                if word[i] == char:
                    continue
                words.append(left + char + right)
        return words
#主函数
if __name__ == '__main__':
    start = "hit"
    end = "cog"
    dict = {"hot", "dot", "dog", "lot", "log"}
    print("start是：", start)
    print("end是：", end)
    print("dict是：", dict)
    solution = Solution()
    print("它的长度是：", solution.ladderLength(start, end, dict))