class Solution():
    def charuSort(self, List):
        size = len(List)
        for i in range(1, size):
            for j in range(i - 1, -1, -1):
                if List[j] > List[j + 1]:
                    List[j], List[j + 1] = List[j + 1], List[j]
                else:
                    break

if __name__ == '__main__':
    solution = Solution()
    List = [3, 2, 4, 5, 1, 8, 6, 9, 7]
    solution.charuSort(List)
    print(List)