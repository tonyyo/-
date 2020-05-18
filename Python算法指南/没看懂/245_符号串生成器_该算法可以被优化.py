class Solution:
    def getIdx(self, c):
        return ord(c) - ord('A')

    def nonTerminal(self, c):
        return ord(c) >= ord('A') and ord(c) <= ord('Z')

    def isMatched(self, s, pos, gen, sym):
        if pos == len(s):
            if len(gen) == 0:
                return True
            else:
                return False
        else:
            if len(gen) == 0:
                return False
            elif self.nonTerminal(gen[0]):
                idx = self.getIdx(gen[0])
                for i in sym[idx]:
                    if self.isMatched(s, pos, i + gen[1:], sym):
                        return True
            elif gen[0] == s[pos]:
                if self.isMatched(s, pos + 1, gen[1:], sym):
                    return True
            else:
                return False
        return False

    def canBeGenerated(self, generator, startSymbol, symbolString):
        sym = [[] for i in range(26)]
        for i in generator:
            sym[self.getIdx(i[0])].append(i[5:])
        idx = self.getIdx(startSymbol)
        for i in sym[idx]:
            if self.isMatched(symbolString, 0, i, sym):
                return True
        return False


# 主函数
if __name__ == '__main__':
    generator = ["S -> abc", "S -> aA", "A -> b", "A -> c"]
    startSymbol = "S"
    symbolString = "ac"
    solution = Solution()
    print("generator是：", generator, "startSymbol是：", startSymbol, "symbolString是：", symbolString)
    print("是否可以被生成", solution.canBeGenerated(generator, startSymbol, symbolString))
