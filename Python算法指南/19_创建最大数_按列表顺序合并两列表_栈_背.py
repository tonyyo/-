class Solution:
    def maxNumber(self, list1, list2, k):
        finalList = []
        for i in range(k + 1):
            tempList1 = self.getMax(list1, i)
            tempList2 = self.getMax(list2, k - i)
            mergeList = [max(tempList1, tempList2).pop(0) for _ in tempList1 + tempList2]
            finalList = max(finalList, mergeList)  # 列表比较大小
        return finalList

    def getMax(self, list1, count):
        stack = []
        for i in range(len(list1)):
            while stack and len(list1) - i + len(stack) > count and list1[i] > stack[-1]:
                stack.pop()
            stack.append(list1[i])
        return stack



    # def getMax(self, list1, count):
    #     dict = {v : k for k, v in enumerate(list1)}
    #     dict = sorted(dict.items(), reverse=True)  # 字典排序后直接会转化成列表类型
    #     dict = {k : v for k, v in dict}  # 转换为字典
    #     splitDict = {k : dict[k] for k in list(dict.keys())[0:count]}  # 字典伪切片的实现
    #     splitDict = sorted(splitDict.items(), key=lambda x : x[1])  # 字典按值排序
    #     splitDict = {k : v for k, v in splitDict}
    #     return list(splitDict.keys())

if __name__ == '__main__':
    solution = Solution()
    list1 = [3, 4, 6, 5]
    list2 = [9, 1, 2, 5, 8, 3]
    k = 5
    print(solution.maxNumber(list1, list2, k))
