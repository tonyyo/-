class Solution():
    def charuSort(self, List):
        size = len(List)
        for i in range(1, size):
            for j in range(i - 1, -1, -1):
                if List[j + 1] < List[j]:
                    List[j + 1], List[j] = List[j], List[j + 1]
                else:
                    break


if __name__ == '__main__':
    solution = Solution()
    List = list(map(int, input().strip().split(',')))
    solution.charuSort(List)
    print(List)