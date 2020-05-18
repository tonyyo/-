class Solution():
    def quickSort(self, start, end, List):
        left, right = start, end # 需要重新定义首尾指针，以便下一层遍历
        if left >= right:   # 当首尾指针重叠，表明只剩下一个元素，程序结束
            return
        pivot = List[start]
        while left < right:
            while left < right and List[right] > pivot: # 先进行右边指针的移动，不然left指针会移动到最右边
                right -=1
            while left < right and List[left] <= pivot: # 那么中间元素就会变成最后一个元素
                left += 1
            if left < right:                            # 也就是说中间元素允许是第一个元素，不允许是最后一个元素
                List[left], List[right] = List[right], List[left]
        List[left], List[start] = List[start], List[left]  # 首元素为哨兵，需要交换和中间元素的位置
        self.quickSort(start, right - 1, List) # left - 1， right + 1正好切分了数组
        self.quickSort(left + 1, end, List)


if __name__ == '__main__':
    List = [3, 2, 1, 4, 5, 9, 20, 7]
    solution = Solution()
    solution.quickSort(0, len(List) - 1, List)
    print(List)