class Solution:
    def multiSort(self, array):
        array.sort(key=lambda x: (-x[1], x[0]))
        return array
#主函数
if __name__ == '__main__':
    array = [[2, 50], [1, 50], [3, 100], ]
    print('初始数组：', array)
    solution = Solution()
    print('结果：', solution.multiSort(array))