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

    def canBeGenerated(self, generator, startSymbol, symbolString):
        dict = {}
        dict2 = {}
        for x in generator:
            tempList = x.split(' -> ')
            if tempList[0] not in dict.keys():
                dict[tempList[0]] = []
                dict[tempList[0]].append(tempList[1])
            else:
                dict[tempList[0]].append(tempList[1])
        print(dict)
        for key in dict.keys():  # 遍历每一个字典中的key对应的value里面是否还有取代符号
            for val in dict[key]:  # val表示其中的一个字符串
                flag = False
                for x in val:
                    if x in dict.keys():  # 如果有大写字母
                        for y in dict[x]:
                            tempval = val
                            tempval = tempval.replace(x, y) # 将大写字母替换
                            if key not in dict2.keys():
                                dict2[key] = []
                                dict2[key].append(tempval)
                            else:
                                dict2[key].append(tempval)
                        flag = True
                if flag == True:
                    continue
                if key not in dict2.keys():
                    dict2[key] = []
                    dict2[key].append(val)
                else:
                    dict2[key].append(val)
        print(dict2)
        if symbolString in dict2[startSymbol]:
            return True
        else:
            return False


# 主函数
if __name__ == '__main__':
    generator = ["S -> abc", "S -> aA", "A -> b", "A -> c"]
    startSymbol = "S"
    symbolString = "ac"
    solution = Solution()
    print("generator是：", generator, "startSymbol是：", startSymbol, "symbolString是：", symbolString)
    print("是否可以被生成", solution.canBeGenerated(generator, startSymbol, symbolString))
