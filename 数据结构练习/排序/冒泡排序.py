class Solution():
    def bubbleSort(self, List):
        size = len(List)
        for i in range(size): # n 次冒泡
            for j in range(1, size - i):  # 每次冒泡的范围逐渐减小
                if List[j - 1] > List[j]: # 正序冒泡
                    List[j], List[j - 1] = List[j - 1], List[j]
        return List
if __name__ == '__main__':
    List = [3, 2, 4, 5, 1, 8, 6, 9, 7]
    solution = Solution()
    print(solution.bubbleSort(List))