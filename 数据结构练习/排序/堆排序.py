class Solution:
    def heapSort(self, List):
        size = len(List)
        for i in range(size - 1, -1, -1):
            self.buildHeap(List, i) # 对前i个数建堆
            List[0], List[i] = List[i], List[0]
        return List

    def buildHeap(self, List, i): # i 表示堆的最后一个元素
        parent = (i - 1) // 2
        for j in range(parent, -1, -1):
            left, right = j * 2 + 1, j * 2 + 2
            if right <= i: # 判断是够有右节点
                maxValueIndex = right if List[right] >= List[left] else left
                if List[maxValueIndex] > List[j]:
                    List[j], List[maxValueIndex] = List[maxValueIndex], List[j]
                else:
                    continue
            else:
                if List[left] > List[j]:
                    List[j], List[left] = List[left], List[j]
                else:
                    continue

if __name__ == '__main__':
    List = [3, 2, 4, 5, 1, 8, 6, 9, 7]
    solution = Solution()
    print(solution.heapSort(List))
