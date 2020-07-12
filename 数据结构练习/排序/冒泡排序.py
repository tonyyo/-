class Solution():
    def maopaoSort(self, List):
        size = len(List)
        for j in range(size):
            for i in range(1, size - j):
                if List[i] < List[i - 1]:
                    List[i], List[i - 1] = List[i - 1], List[i]
        return List
if __name__ == '__main__':
    List = [3, 2, 4, 5, 1, 8, 6, 9, 7]
    solution = Solution()
    print(solution.maopaoSort(List))