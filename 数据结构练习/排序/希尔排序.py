class Solution():
    def shellSorted(self, List):
        size = len(List)
        length = size // 2
        while length != 0:
            for i in range(length, size, length):
                for j in range(i - length, -1, -length):
                    if List[j] > List[j + length]:
                        List[j], List[j + length] = List[j + length], List[j]
            length //= 2

    def shellSorted2(self, List):
        size = len(List)
        length = size // 2
        while length != 0:
            for i in range(size - length):
                if List[i] > List[i + length]:
                    List[i], List[i + length] = List[i + length], List[i]
            length //= 2

if __name__ == '__main__':
    List = [3, 2, 4, 5, 1, 8, 6, 9, 7]
    solution = Solution()
    solution.shellSorted(List)
    print(List)