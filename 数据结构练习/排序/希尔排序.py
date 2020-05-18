class Solution():
    def shellSorted(self, List):
        size = len(List)
        length = size // 2
        while length != 0:
            for i in range(size - length):
                if List[i] > List[i + length]:
                    List[i], List[i + length] = List[i + length], List[i]
            length //= 2

if __name__ == '__main__':
    List = list(map(int, input().strip().split(',')))
    solution = Solution()
    solution.shellSorted(List)
    print(List)