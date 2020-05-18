from itertools import combinations, permutations


class Solution:
    def wordSquares(self, words):
        ans = []
        results = list(permutations(words, 4)) # 从words中取出4个数进行全排列
        for x in results:
            if self.is_dancijuzhen(x) and x not in ans:
                ans.append(x)
        return ans

    def is_dancijuzhen(self, words):
        size = len(words)
        for i in range(size):
            for j in range(size):
                if words[i][j] != words[j][i]: # 判断是否是单词矩阵
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