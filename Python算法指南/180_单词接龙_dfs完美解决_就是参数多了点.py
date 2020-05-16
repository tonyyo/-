from collections import deque
class Solution:
    def findLadders(self, start, end, dict):
        dict.add(start)
        dict.add(end)
        indexes = self.build_indexes(dict)
        distance = {}
        self.bfs(end, start, distance, indexes)
        results = []
        self.dfs(start, end, distance, indexes, [start], results)
        return results

    def build_indexes(self, dict):
        indexes = {}
        for word in dict:
            for i in range(len(word)):
                key = word[:i] + '%' + word[i + 1:]
                if key in indexes:
                    indexes[key].add(word)
                else:
                    indexes[key] = set([word])
        return indexes

    def bfs(self, start, end, distance, indexes):
        distance[start] = 0
        queue = deque([start])
        while queue:
            word = queue.popleft()
            for next_word in self.get_next_words(word, indexes):
                if next_word not in distance:
                    distance[next_word] = distance[word] + 1
                    queue.append(next_word)

    def get_next_words(self, word, indexes):
        words = []
        for i in range(len(word)):
            key = word[:i] + '%' + word[i + 1:]
            for w in indexes.get(key, []):
                words.append(w)
        return words

    def dfs(self, curt, target, distance, indexes, path, results):
        if curt == target:
            results.append(list(path))
            return
        for word in self.get_next_words(curt, indexes):
            if distance[word] != distance[curt] - 1:
                continue
            path.append(word)
            self.dfs(word, target, distance, indexes, path, results)
            path.pop()

    def findLadders2(self, start, end, dict, ans, results):
        if self.findOneDiff(start, end):
            results.append(ans + [end])
            return
        targets = self.findOneDiffList(start, dict)
        for x in targets:
            dict.remove(x)
        for x in targets:
            start = x
            ans.append(x)
            self.findLadders2(start, end, dict, ans, results)
            ans.remove(x)
        for x in targets:
            dict.add(x)

    def findOneDiffList(self, string1, set):
        ans = []
        for x in set:
            count = 0
            for i in range(len(x)):
                if string1[i] != x[i]:
                    count += 1
            if count == 1:
                ans.append(x)
        return ans

    def findOneDiff(self, string1, string2):
        count = 0
        for i in range(len(string1)):
            if string1[i] != string2[i]:
                count += 1
        if count == 1:
            return True
        else:
            return False


# 主函数
if __name__ == '__main__':
    start = "hit"
    end = "cog"
    dict = set(["hot", "dot", "dog", "lot", "log"])
    print("start是：", start)
    print("end是：", end)
    print("dict是：", dict)
    solution = Solution()
    ans = [start]
    results = []
    solution.findLadders2(start, end, dict, ans, results)
    minLenResults = []
    for x in results:
        if len(minLenResults) == 0:
            minLenResults.append(x)
        elif len(x) < len(minLenResults[0]):
            minLenResults.clear()
            minLenResults.append(x)
        elif len(x) == len(minLenResults[0]):
            minLenResults.append(x)
    print(minLenResults)


