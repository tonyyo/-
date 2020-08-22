class Solution():
    def shellSorted(self, List):
        size = len(List)
        length = size // 2  # 初始步长
        while length != 0:
            for i in range(size - length):  # 步长减小, 插入排序的范围逐渐变大
                if List[i] > List[i + length]:
                    List[i], List[i + length] = List[i + length], List[i]
            length //= 2

if __name__ == '__main__':
    List = [3, 2, 4, 5, 1, 8, 6, 9, 7]
    solution = Solution()
    solution.shellSorted(List)
    print(List)