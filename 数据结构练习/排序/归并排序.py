class Solution():
    def mergeSort(self, left, right, List):
        if left >= right:
            return List[left : right + 1]
        mid = (left + right) // 2
        leftList = self.mergeSort(left, mid, List)
        rightList = self.mergeSort(mid + 1, right, List)
        return self.merge(leftList, rightList)

    def merge(self, leftList, rightList):
        resultList = []
        lSize, rSize = len(leftList), len(rightList)
        i, j = 0, 0
        while i < lSize and j < rSize:
            if leftList[i] < rightList[j]:
                resultList.append(leftList[i])
                i += 1
            else:
                resultList.append(rightList[j])
                j += 1
        while i < lSize:
            resultList.append(leftList[i])
            i += 1
        while j < rSize:
            resultList.append(rightList[j])
            j += 1
        return resultList

if __name__ == '__main__':
    List = [3, 2, 4, 5, 1, 8, 6, 9, 7]
    solution = Solution()
    print(solution.mergeSort(0, len(List) - 1, List))