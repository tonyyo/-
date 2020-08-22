class Solution():
    def insertSort(self, List):
        size = len(List)
        for i in range(1, size): # n - 1次插入, 因为默认第一个元素已经插入好
            for j in range(i - 1, -1, -1): # 将当前元素List[i]插入List[:i]
                if List[j] > List[j + 1]:  # 与其说是插入排序, 不如说是相邻交换排序
                    List[j], List[j + 1] = List[j + 1], List[j]
                else:
                    break

if __name__ == '__main__':
    solution = Solution()
    List = [3, 2, 4, 5, 1, 8, 6, 9, 7]
    solution.charuSort(List)
    print(List)