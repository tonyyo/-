class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word_list = []


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            node.word_list.append(word)
        node.is_word = True

    def find(self, word):
        node = self.root
        for c in word:
            node = node.children.get(c)
            if node is None:
                return None
        return node

    def get_words_with_prefix(self, prefix):
        node = self.find(prefix)
        return [] if node is None else node.word_list

    def contains(self, word):
        node = self.find(word)
        return node is not None and node.is_word


class Solution:
    # 参数words代表没有重复的一系列单词集合
    # 返回所有单词矩阵
    def wordSquares2(self, words):
        trie = Trie()
        for word in words:
            trie.add(word)
        squares = []
        for word in words:
            self.search(trie, [word], squares)
        return squares

    def search(self, trie, square, squares):
        n = len(square[0])
        curt_index = len(square)
        if curt_index == n:
            squares.append(list(square))
            return
        # 修剪，可以删除它，但会比较慢
        for row_index in range(curt_index, n):
            prefix = ''.join([square[i][row_index] for i in range(curt_index)])
            if trie.find(prefix) is None:
                return
        prefix = ''.join([square[i][curt_index] for i in range(curt_index)])
        for word in trie.get_words_with_prefix(prefix):
            square.append(word)
            self.search(trie, square, squares)
            square.pop()  # remove the last word

    def is_dancijuzhen(self, words):
        size = len(words)
        for i in range(size):
            for j in range(size):
                if words[i][j] != words[j][i]:
                    return False
        return True


# 主函数
if __name__ == '__main__':
    word = ["area", "lead", "wall", "lady", "ball", "ssss"]
    print("单词序列是：", word)
    solution = Solution()
    ans = []
    ans = solution.wordSquares(word)
    for x in ans:
        print(x)