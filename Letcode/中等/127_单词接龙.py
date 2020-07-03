import collections
import copy


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        neighborList = dict()     # 邻接表是字典类型，key存节点，value存出度点集合
        headList = copy.deepcopy(wordList)  # 深拷贝，互不影响
        headList.insert(0, beginWord)
        for head in headList:       # keys
            if head == endWord:
                continue
            tempList = []
            for node in wordList:
                if self.diff(head, node): # 字母相差1位并且之前没用到过, 但beginword不算
                    tempList.append(node)
            if len(tempList) != 0:  # 为空的话没意义
                neighborList[head] = tempList
        queue = collections.deque()
        queue.append(beginWord)
        minLen = 1
        visit = [beginWord]
        while queue:
            length = len(queue)
            for _ in range(length):
                pos = queue.popleft()
                if pos == endWord:  # bfs遍历到目标点，就是最短路径点
                    return minLen
                if neighborList.get(pos):  # 必须判断是否存在，否则浏览器报keyError
                    for node in neighborList.get(pos):
                        if node not in visit:
                            queue.append(node)
                            visit.append(node)
            minLen += 1
        return 0

    def diff(self, word1, word2):
        diff = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                diff += 1
        return True if diff == 1 else False

if __name__ == '__main__':
    solution = Solution()
    beginWord = "leet"
    endWord = "code"
    wordList = ["lest","leet","lose","code","lode","robe","lost"]
    print(solution.ladderLength(beginWord, endWord, wordList))