class Solution:
    def findMin(self, num):
        min = num[0]
        start, end = 0, len(num) - 1
        while start < end:
            mid = (start + end) // 2
            if num[mid] > num[end]:
                start = mid + 1
            elif num[mid] < num[end]:
                end = mid
        return num[start]

if __name__ == '__main__':
    temp = Solution()
    List1 = [5, 6, 7, 8, 1, 2, 4]
    print(("输入：" + str(List1)))
    print(("输出：" + str(temp.findMin(List1))))
