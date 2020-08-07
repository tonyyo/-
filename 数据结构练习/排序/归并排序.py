
class Solution():
    def mergeSort(self, left, right, List):  # 归并排序
        if left >= right:   # 最终排序还是剩一个元素时，排序完成，然后利用merge进行排序
            return List[left : right + 1]
        mid = (left + right) // 2
        leftList = self.mergeSort(left, mid, List)
        rightList = self.mergeSort(mid + 1, right, List)
        return self.merge(leftList, rightList)

    def merge(self, leftList, rightList):
        resultList = []
        while leftList and rightList:
            if leftList[0] < rightList[0]:
                resultList.append(leftList.pop(0))
            else:
                resultList.append(rightList.pop(0))
        resultList += leftList
        resultList += rightList
        return resultList

if __name__ == '__main__':
    List = [3, 2, 4, 5, 1, 8, 6, 9, 7]
    solution = Solution()
    print(solution.mergeSort(0, len(List) - 1, List))