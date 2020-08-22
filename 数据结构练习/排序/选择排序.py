class Solution():
    def selectSort(self, List):
        size = len(List)
        for i in range(size): # n 次选择
            for j in range(i + 1, size): # 选择的范围逐渐缩小
                if List[i] > List[j]:
                    List[i], List[j] = List[j], List[i]

if __name__ == '__main__':
    solution = Solution()
    List = list(map(int, input().strip().split(',')))
    solution.selectSort(List)
    print(List)